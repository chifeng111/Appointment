import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from .models import ConfeRoom, Order
from django.contrib import messages
from .forms import Logi_form, Register_form, Add_form

#显示可用会议室
def list(request):
    room = ConfeRoom.objects.all()
    content = {
        'room': room
    }
    return render(request, 'list.html', content)

#某个会议室预约详情
def appointment(request, id):
    room = get_object_or_404(ConfeRoom, id=id)
    d = datetime.date.today()
    order = Order.objects.filter(room=room, time__gte=d).order_by('time')
    content = {
        'order': order,
        'room': room
    }
    return render(request, 'order.html', content)

def logi(request):
    form = Logi_form()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        u = authenticate(username=username, password=password)
        if u and u.is_active:
            login(request, u)
            return redirect('conferance:list')

    content = {
        'form': form
    }
    return render(request, 'logi.html', content)

def logo(request):
    if request.user.is_active:
        logout(request)
        return redirect('conferance:list')

def register(request):
    form = Register_form(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user.username = username
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return redirect('conferance:list')

    content = {
        'form': form
    }
    return render(request, 'logi.html', content)

def add(request, id):
    if not request.user.is_active:
        return redirect('conferance:register')

    form = Add_form(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.room = ConfeRoom.objects.get(id=id)
        order_list = Order.objects.filter(room=instance.room)
        time_list = []
        for order in order_list:
            time_list.append(order.time)
        if instance.time not in time_list:
            if date_is_valid(instance.time):
                instance.save()
                return redirect('/conferance/%s' %id)
            else:
                messages.error(request, '超出预约范围')
                return redirect('/conferance/%s' % id)
        else:
            messages.error(request,'该时间已被预约')
            return redirect('/conferance/%s' % id)

    context = {
        "form": form,
    }
    return render(request, 'logi.html', context)

def delete(request, room_id, order_id):
    order = get_object_or_404(Order,id=order_id)
    if order.user != request.user:
        raise Http404
    order.delete()
    messages.success(request,'删除成功！')
    return redirect('/conferance/%s' % room_id)

#设置预约范围，判断是否合法
def date_is_valid(date):
    d1 = datetime.date.today()
    d2 = d1 + datetime.timedelta(days=15)
    if date >= d1 and date < d2:
        return True
    else:
        return False
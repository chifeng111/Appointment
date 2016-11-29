from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import ConfeRoom, Order
from .forms import Logi_form

# Create your views here.
def list(request):
    room = ConfeRoom.objects.all()
    content = {
        'room': room
    }
    return render(request, 'list.html', content)

def appointment(request, id):
    room = get_object_or_404(ConfeRoom, id=id)
    order = Order.objects.filter(room=room)
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
    pass
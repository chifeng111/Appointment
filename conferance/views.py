from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ConfeRoom, Order

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
    pass

def logo(request):
    pass

def register(request):
    pass
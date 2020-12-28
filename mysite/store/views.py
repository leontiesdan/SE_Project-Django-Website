from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from datetime import datetime 
from .models import *

def home(request):
    return render(request, 'store/home.html', None)

class AlbumView(generic.ListView):
    template_name = 'store/albums.html'
    context_object_name = 'albums_all'

    def get_queryset(self):
        """Return the last five published questions."""
        return Album.objects.all()

def cartView(request):
    if request.method == "GET":
        (Profile.objects.get(user= request.user)).cartAlbums.set((Profile.objects.get(user= request.user)).cartAlbums.exclude(slug=request.GET.get("remove_item", "")))
    if request.method == "POST":
        total = float(request.POST.get("buy_item", ""))
        user_balance = Profile.objects.get(user= request.user).balance
        if total <= user_balance:
            Profile.objects.filter(user= request.user).update(balance=(user_balance-total))
            createdOrder = Order.objects.create(buyer=Profile.objects.get(user= request.user), date=datetime.now())
            for albumCart in (Profile.objects.get(user= request.user)).cartAlbums.all():
                AlbumInstance.objects.create(album= albumCart, order = createdOrder)
            Profile.objects.get(user= request.user).cartAlbums.set([])
    return render(request, 'store/cart.html', {
                'cart_items': Profile.objects.get(user= request.user).cartAlbums.all(),
                'total_price': sum([x.price for x in Profile.objects.get(user= request.user).cartAlbums.all()])
            })


def albumDetailView(request, slug):
    if request.method == "GET":
        (Profile.objects.get(user= request.user)).cartAlbums.add(Album.objects.get(slug=slug))
    return render(request, 'store/detail.html', {'album': Album.objects.get(slug=slug)})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('store:login')
    template_name = 'registration/signup.html'

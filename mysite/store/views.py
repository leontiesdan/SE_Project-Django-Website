from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import *

def home(request):
    return render(request, 'store/home.html', None)

class AlbumView(generic.ListView):
    template_name = 'store/albums.html'
    context_object_name = 'albums_all'

    def get_queryset(self):
        """Return the last five published questions."""
        return Album.objects.all()

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'store/detail.html'


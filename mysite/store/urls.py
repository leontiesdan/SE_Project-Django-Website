from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('home', views.home, name='home'),
    path('albums', views.AlbumView.as_view(), name="albums"),
    path('albums/<slug>', views.AlbumDetailView.as_view(), name='detail'),

]
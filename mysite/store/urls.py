from django.urls import include, path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('albums', views.AlbumView.as_view(), name="albums"),
    path('albums/<slug>', views.AlbumDetailView.as_view(), name='detail'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
]
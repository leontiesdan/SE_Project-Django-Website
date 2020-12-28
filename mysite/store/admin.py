from django.contrib import admin
from .models import Genre, Band, Album, Order, AlbumInstance, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'cover', 'display_price', 'description', 'display_genre', 'band')
	prepopulated_fields = {'slug': ('name',)} # new	

class OrderAdmin(admin.ModelAdmin):
	list_display = ('date', 'get_total', 'get_items')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)    
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumInstance)
admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Profile)
admin.site.register(Order, OrderAdmin)
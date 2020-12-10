from django.contrib import admin
from .models import Genre, Band, Album, Order, AlbumInstance

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'cover', 'display_price', 'description', 'display_genre', 'band')

class OrderAdmin(admin.ModelAdmin):
	list_display = ('date', 'get_total')


admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumInstance)
admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Order, OrderAdmin)
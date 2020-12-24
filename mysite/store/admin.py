from django.contrib import admin
from .models import Genre, Band, Album, Order, AlbumInstance

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'cover', 'display_price', 'description', 'display_genre', 'band')
	prepopulated_fields = {'slug': ('name',)} # new	

class OrderAdmin(admin.ModelAdmin):
	list_display = ('date', 'get_total', 'get_items')


admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumInstance)
admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Order, OrderAdmin)
from django.db import models
import uuid
# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Band(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length = 400)
	def __str__(self):
		return self.name

class Album(models.Model):
	name = models.CharField(max_length=100)
	cover = models.ImageField(upload_to='store/static/store/images')
	price = models.PositiveIntegerField(default = 0)
	description = models.CharField(max_length=400)
	genre = models.ManyToManyField(Genre)
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	slug = models.SlugField(max_length = 250, unique=True) 
	def get_local_url(self):
		return self.cover.url.rsplit('/', 1)[1]
	def display_price(self):
		return str(self.price) + " €"
	def display_genre(self):
		return ', '.join(genre.name for genre in self.genre.all())
	display_genre.short_description = "Genre"
	def __str__(self):
		return self.name

class AlbumInstance(models.Model):
	uuid = models.UUIDField(unique=True, default=uuid.uuid4, help_text='Unique ID for this album instance')
	album = models.ForeignKey('Album', on_delete = models.SET_NULL, null = True)
	order = models.ForeignKey('Order', on_delete = models.SET_NULL, null = True)
	def __str__(self):
		return self.album.name

class Order(models.Model):
	uuid = models.UUIDField(unique=True, default=uuid.uuid4, help_text='Unique ID for this order instance')
	date = models.DateTimeField('date ordered')
	def get_total(self):
		total = 0
		for instance in AlbumInstance.objects.filter(order_id = self.id):
			total += Album.objects.get(name=instance.album).price
		return total
	def get_items(self):
		return [str(x) for x in AlbumInstance.objects.filter(order_id = self.id)]
	def __str__(self):
		return str(self.id)
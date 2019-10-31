from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Categoria(models.Model):
	nombre = models.CharField(max_length=50, help_text='nombre de la categoría. Ejemplo: Padres, Alumnos, ..')
	slug = models.SlugField(max_length=50, editable=False)

	def slug(self):
		return slugify(self.nombre)

	def __str__(self):
		return self.nombre


class Novedad(models.Model):
	titulo = models.CharField(max_length=255, help_text='ingrese el titulo de la novedad')
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	contenido = RichTextField()
	imagen = models.ImageField(upload_to='asesoria/novedades', blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
	fecha_alta = models.DateTimeField(auto_now_add=True)
	fecha_modificado = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=255, editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = 'novedades'
		ordering = ['-fecha_alta']

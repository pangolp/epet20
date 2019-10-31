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

	class Meta:
		verbose_name_plural = 'categorias'


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


class Asesora(models.Model):
	nombre = models.CharField(max_length=100, help_text='nombre de la asesora')
	apellido = models.CharField(max_length=100, help_text='apellido de la asesora')
	email = models.EmailField(help_text='correo de contacto', blank=True, null=True)
	foto = models.ImageField(upload_to='asesoria/asesoras', blank=True, null=True)

	def __str__(self):
		return '%s, %s' % (self.apellido, self.nombre)

	class Meta:
		verbose_name_plural = 'asesoras'


DIA_CHOICES = (
	('lunes', 'Lunes'),
	('martes', 'Martes'),
	('miercoles', 'Miércoles'),
	('jueves', 'Jueves'),
	('viernes', 'Viernes')
)


class Horario(models.Model):
	asesora = models.ForeignKey(Asesora, on_delete=models.CASCADE)
	dia = models.CharField('dia de la semana', max_length=50, choices=DIA_CHOICES)
	horario_inicio = models.TimeField('horario de llegada')
	horario_fin = models.TimeField('horario de salida')

	def __str__(self):
		return '%s, %s' % (self.asesora.apellido, self.asesora.nombre)

	class Meta:
		verbose_name_plural = 'horarios'
		unique_together = ['asesora', 'dia', 'horario_inicio', 'horario_fin']

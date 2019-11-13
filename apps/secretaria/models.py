# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Categoria(models.Model):
	nombre = models.CharField(max_length=50, help_text='nombre de la categoría. Ejemplo: Padres, Alumnos, ..')
	slug = models.SlugField(max_length=50, editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'categorias'


class Novedad(models.Model):
	titulo = models.CharField(max_length=255, help_text='ingrese el titulo de la novedad')
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	contenido = RichTextField()
	imagen = models.ImageField(upload_to='secretaria/novedades', blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='user_novedad')
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


class Materia(models.Model):

	nombre = models.CharField(
		max_length=50,
		help_text='Ingrese el nombre de la materia.'
	)

	año = models.PositiveSmallIntegerField(
		validators=[
			MaxValueValidator(6),
			MinValueValidator(1)
		],
		help_text='Ingrese el año de la materia.'
	)

	fecha_hora = models.DateTimeField(
		'Fecha y Hora',
		help_text='Ingrese la fecha y hora a la que se rinde la materia. Formato: "DD/MM/AAAA HH:MM"'
	)

	aula = models.CharField(
		max_length=50,
		help_text='Ingrese el aula en la que se rinde la materia.'
	)

	profesores = models.CharField(
		max_length=150,
		help_text='Ingrese los profesores que evaluarán. Formato: "Nombre Apellido, Nombre Apellido, etc."'
	)

	class Meta:
		verbose_name='Materia'
		verbose_name_plural='Materias'

	def __str__(self):
		return '%s - %s Año' % (self.nombre, self.año)


class RegistroMesaExamen(models.Model):
	nombre = models.CharField(max_length=40, help_text='Ingrese el nombre del alumno')
	apellido = models.CharField(max_length=40, help_text='Ingrese el apellido del alumno')
	dni = models.PositiveIntegerField(
		help_text='Ingrese el dni del alumno',
		validators=[
			MaxValueValidator(999999999),
			MinValueValidator(1000000)
		]
	)
	materia = models.ForeignKey(Materia, on_delete=models.CASCADE, help_text='Ingrese un materia a rendir') #Hay que hacer un ForeignKey (esperar a nahuel que suba sus cambios)
	correo_electronico = models.CharField(max_length=100, help_text='Ingrese un correo electronico para poder comunicarnos con el alumno')

	class Meta:
		verbose_name='registro para mesa de examen'
		verbose_name_plural='registros para mesas de examenes'

	def __str__(self):
		return '%s %s %s' % (self.nombre, self.apellido, self.materia)

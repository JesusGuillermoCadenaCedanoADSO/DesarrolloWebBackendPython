from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    # se ejecuta la primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    # se ejecuta cada vez que se actualiza una instancia
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        #campo de ordenacion se incluye el guion para ordenar de
        #mas reciente a mas antiguo
        ordering = ["-created"]
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación",default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    # se ejecuta la primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    # se ejecuta cada vez que se actualiza una instancia
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        #campo de ordenacion se incluye el guion para ordenar de
        #mas reciente a mas antiguo
        ordering = ["-created"]
    
    def __str__(self):
        return self.title

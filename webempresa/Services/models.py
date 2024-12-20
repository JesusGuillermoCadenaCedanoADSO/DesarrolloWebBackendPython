from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.TextField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to="services")
    # se ejecuta la primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    # se ejecuta cada vez que se actualiza una instancia
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        #campo de ordenacion se incluye el guion para ordenar de
        #mas reciente a mas antiguo
        ordering = ["-created"]
    
    def __str__(self):
        return self.title

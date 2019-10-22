from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre

class Integrante(models.Model):
    """Model definition for Integrante."""
    nombre = models.CharField(max_length=50)
    especialidad = models.TextField(blank=True, null=True)

    def __str__(self):
        """Unicode representation of Integrante."""
        return self.nombre

class Imagenes(models.Model):
    """Model definition for Imagenes."""
    id = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to="imagenes")

    def __str__(self):
        """Unicode representation of Imagenes."""
        return str(self.id)

    def get_image_url(self):
        return self.imagen.url

class AsignarIntegrante(models.Model):
    """Model definition for AsignarIntegrante."""
    integrante=models.ForeignKey(Integrante,on_delete=models.PROTECT)
    proyecto=models.ForeignKey("Proyecto",on_delete=models.PROTECT)
    

class AsignarImagenes(models.Model):
    """Model definition for AsignarIntegrante."""
    imagenes=models.ForeignKey(Imagenes,on_delete=models.PROTECT)
    proyecto=models.ForeignKey("Proyecto",on_delete=models.PROTECT)
    


class Proyecto(models.Model):
    """Model definition for Proyecto."""
    imagen = models.ImageField(upload_to="proyectos")
    nombre = models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    integrante=models.ManyToManyField(Integrante,through=AsignarIntegrante)
    imagenes=models.ManyToManyField(Imagenes, through=AsignarImagenes)
    
    def get_inte_values(self):
        ret = ''
        print(self.integrante.all())
    # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for integrante in self.integrante.all():
            ret = ret + integrante.nombre + ', '
    # remove the last ',' and return the value.
        return str(ret[:-1])
    
    def __str__(self):
        """Unicode representation of Proyecto."""
        return str(self.nombre)

    def get_absolute_url(self):
        return u'/proyectos/%d' % self.id 

    def get_image_url(self):
        return self.imagen.url





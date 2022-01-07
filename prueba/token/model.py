from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Token(models.Model):

    idToken=models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    valor=models.CharField(max_length=6)
    fechaRegistro = models.DateTimeField(auto_now_add=True, blank=True)

    


    def __str__(self):
        """Return company and first_name and last_name."""
        return f'{self.valor}'
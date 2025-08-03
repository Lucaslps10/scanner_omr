from django.db import models

# Create your models here.

class UploadOMR(models.Model):
    imagem = models.ImageField(upload_to='uploads/')
    nota = models.FloatField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultado: {self.nota}% em {self.data_envio.strftime('%d/%m/%Y')}"


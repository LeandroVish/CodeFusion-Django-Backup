from django.db import models


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.nome}"
from django.db import models

class Avaliacao(models.Model):
    titulo = models.CharField(max_length=350, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%d - %s' %(self.id, self.titulo)

class Pergunta(models.Model):
    nome = models.CharField(max_length=350, unique=True)
    avaliacao_id = models.ForeignKey(to=Avaliacao, on_delete=models.CASCADE)

class Resposta(models.Model):
    nome = models.CharField(max_length=350, unique=True)
    pergunta_id = models.ForeignKey(to=Pergunta, on_delete=models.CASCADE)

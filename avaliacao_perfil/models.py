from django.db import models

class Avaliacao(models.Model):
    titulo = models.CharField(max_length=350, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    nome = models.CharField(max_length=350, unique=True)
    avaliacao_id = models.ForeignKey(to=Avaliacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Comportamento(models.Model):
    nome = models.CharField(max_length=350, unique=True)

    def __str__(self):
        return self.nome

class PontoForte(models.Model):
    nome = models.CharField(max_length=350, unique=True)

    def __str__(self):
        return self.nome

class PontoDaMelhoria(models.Model):
    nome = models.CharField(max_length=350, unique=True)

    def __str__(self):
        return self.nome

class Motivacao(models.Model):
    nome = models.CharField(max_length=350, unique=True)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    nome = models.CharField(max_length=350, unique=True)
    descricao = models.TextField(blank=True, null=True)
    imagem_perfil = models.ImageField(upload_to='media/img')
    padrao_comportamento = models.CharField(max_length=450)
    comportamento_id = models.ForeignKey(to=Comportamento, on_delete=models.CASCADE)
    ponto_forte_id = models.ForeignKey(to=PontoForte, on_delete=models.CASCADE)
    ponto_da_melhoria_id = models.ForeignKey(to=PontoDaMelhoria, on_delete=models.CASCADE)
    motivacao_id = models.ForeignKey(to=Motivacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Resposta(models.Model):
    nome = models.CharField(max_length=350, unique=True)
    pergunta_id = models.ForeignKey(to=Pergunta, on_delete=models.CASCADE)
    perfil_id = models.ForeignKey(to=Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

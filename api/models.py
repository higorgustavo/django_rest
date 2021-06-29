from django.db import models


class Tecnologia(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    CONTRATACAO_CHOICE = [
        ("CLT", "Emprego registrado pela CLT"),
        ("PJ", "Pessoa Jurídica")
    ]
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    salario = models.FloatField()
    local = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    contato = models.EmailField()
    tipo_contrato = models.CharField(max_length=3, choices=CONTRATACAO_CHOICE)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo
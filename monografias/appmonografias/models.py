from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.get_full_name()

class Professor(models.Model):
    TITULACAO_CHOICES = [
        ('M', 'Mestre'),
        ('D', 'Doutor'),
        ('P', 'Pós-Doutor'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    titulação = models.CharField(max_length=1, choices=TITULACAO_CHOICES)
    area_pesquisa = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.get_full_name()

class Monografia(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='orientacoes')
    coorientador = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=True, null=True, related_name='coorientacoes')
    resumo = models.TextField()
    abstract = models.TextField()
    palavras_chave = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='monografias/')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo

class Banca(models.Model):
    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('CANCELADA', 'Cancelada'),
        ('REALIZADA', 'Realizada'),
    ]

    monografia = models.ForeignKey(Monografia, on_delete=models.CASCADE)
    professores_avaliadores = models.ManyToManyField(Professor)
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=100)
    nota_final = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='AGENDADA', 
    )

    def __str__(self):
        return f'{self.monografia.titulo} - {self.get_status_display()}'
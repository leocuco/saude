from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class paciente(models.Model):
    escolhas_sexo = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    )

    escolhas_estado_civil = (
        ('Solteiro/a', 'Solteiro/a'),
        ('Casado/a', 'Casado/a'),
        ('Divorciado/a', 'Divorciado/a'),
        ('Viuvo/a', 'Viuvo/a'),
        ('Outro', 'Outro')
    )

    tipo_documento = (
        ('BI','BI'), 
        ('Passaporte','Passaporte'), 
        ('Carta de conducao','Carta de conducao'),
        ('Cartao de eleitor','Cartao de eleitor'), 
        ('DIRE','DIRE'), 
        ('Outro','Outro')
    )

    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=200)
    data_nascimento = models.DateField('data de nascimento')
    sexo = models.CharField(max_length=18, choices=escolhas_sexo)
    local_nascimento = models.CharField(max_length=200, null=True)
    numero_contribuinte = models.IntegerField()
    morada = models.CharField(max_length=200, null=True)
    telefone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profissao = models.CharField(max_length=200, null=True)
    observacoes = models.TextField(null=True)
    tipo_documento = models.CharField(max_length=200, choices=tipo_documento,null=True)
    numero_documento = models.CharField(max_length=200)
    data_emissao_documento = models.DateField('data de emissao', null=True)
    data_validade_documento = models.DateField('data de validade', null=True)
    nacionalidade = models.CharField(max_length=200, null=True)
    estado_civil = models.CharField(max_length=12, choices=escolhas_estado_civil)
    nome_pai = models.CharField(max_length=200, null=True)
    nome_mae = models.CharField(max_length=200, null=True)
    data_criacao = models.DateTimeField('data de criacao',default=timezone.now)
    utilizador_criacao = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='utilizador_criacao')
    ultima_alteracao = models.DateTimeField('ultima alteracao',default=timezone.now)
    inactivo = models.BooleanField(default=False)
    


    def __str__(self):
        return self.nome + ' ' + self.apelido
    
    def idade(self):    
        return datetime.date.today().year - self.data_nascimento.year
    
class medico(models.Model):
    pass
    
   




    




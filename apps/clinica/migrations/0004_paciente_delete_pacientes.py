# Generated by Django 4.2.7 on 2023-11-21 11:53

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinica', '0003_pacientes_inactivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField(verbose_name='data de nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=18)),
                ('local_nascimento', models.CharField(max_length=200)),
                ('numero_contribuinte', models.IntegerField()),
                ('numero_beneficiario', models.IntegerField()),
                ('morada', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('profissao', models.CharField(max_length=200)),
                ('observacoes', models.TextField()),
                ('numero_documento', models.IntegerField()),
                ('data_emissao_documento', models.DateField(verbose_name='data de emissao')),
                ('data_validade_documento', models.DateField(verbose_name='data de validade')),
                ('nacionslidade', models.CharField(max_length=200)),
                ('estado_civil', models.CharField(choices=[('S', 'Solteiro/a'), ('C', 'Casado/a')], max_length=12)),
                ('nome_pai', models.CharField(max_length=200)),
                ('nome_mae', models.CharField(max_length=200)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criacao')),
                ('ultima_alteracao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima alteracao')),
                ('inactivo', models.BooleanField(default=False)),
                ('utilizador_criacao', models.ManyToManyField(related_name='utilizador_criacao', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='pacientes',
        ),
    ]
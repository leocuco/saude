# Generated by Django 4.2.7 on 2024-03-12 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinica', '0012_alter_paciente_estado_civil_alter_paciente_sexo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(null=True)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criacao especialidade')),
                ('ultima_alteracao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima alteracao especialidade')),
                ('inactivo', models.BooleanField(default=False)),
                ('utilizador_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilizador_criacao_especialidade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField(verbose_name='data de nascimento')),
                ('sexo', models.CharField(max_length=200)),
                ('local_nascimento', models.CharField(max_length=200, null=True)),
                ('numero_na_ordem', models.IntegerField()),
                ('validade_cartao_ordem', models.DateField(null=True, verbose_name='data de validade')),
                ('morada', models.CharField(max_length=200, null=True)),
                ('telefone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('observacoes', models.TextField(null=True)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criacao medico')),
                ('ultima_alteracao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima alteracao medico')),
                ('inactivo', models.BooleanField(default=False)),
                ('utilizador_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilizador_criacao_medico', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criacao Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ultima_alteracao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima alteracao paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='utilizador_criacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilizador_criacao_paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='medico_especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de criacao medico_especialidade')),
                ('ultima_alteracao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima alteracao medico especialidade')),
                ('inactivo', models.BooleanField(default=False)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.especialidade')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
                ('utilizador_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilizador_criacao_medico_especialidade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_paciente_delete_pacientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='numero_beneficiario',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_emissao_documento',
            field=models.DateField(null=True, verbose_name='data de emissao'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_validade_documento',
            field=models.DateField(null=True, verbose_name='data de validade'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='local_nascimento',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='morada',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nacionslidade',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nome_mae',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nome_pai',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_documento',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='observacoes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='profissao',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0009_alter_paciente_estado_civil_alter_paciente_sexo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estado_civil',
            field=models.CharField(choices=[('S', 'Solteiro/a'), ('C', 'Casado/a'), ('D', 'Divorciado/a'), ('V', 'Viuvo/a'), ('O', 'Outro')], max_length=12),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipo_documento',
            field=models.CharField(choices=[('B', 'BI'), ('P', 'Passaporte'), ('CC', 'Carta de conducao'), ('CE', 'Cartao de eleitor'), ('D', 'DIRE'), ('O', 'Outro')], max_length=200, null=True),
        ),
    ]

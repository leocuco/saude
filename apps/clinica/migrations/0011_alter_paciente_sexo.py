# Generated by Django 4.2.7 on 2023-11-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0010_alter_paciente_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=18),
        ),
    ]

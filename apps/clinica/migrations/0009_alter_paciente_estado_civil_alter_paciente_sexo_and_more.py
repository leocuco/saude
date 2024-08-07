# Generated by Django 4.2.7 on 2023-11-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0008_alter_paciente_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estado_civil',
            field=models.CharField(choices=[('Solteiro/a', 'Solteiro/a'), ('Casado/a', 'Casado/a'), ('Divorciado/a', 'Divorciado/a'), ('Viuvo/a', 'Viuvo/a'), ('Outro', 'Outro')], max_length=12),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=18),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipo_documento',
            field=models.CharField(choices=[('BI', 'BI'), ('Passaporte', 'Passaporte'), ('Carta de conducao', 'Carta de conducao'), ('Cartao de eleitor', 'Cartao de eleitor'), ('DIRE', 'DIRE'), ('Outro', 'Outro')], max_length=200, null=True),
        ),
    ]

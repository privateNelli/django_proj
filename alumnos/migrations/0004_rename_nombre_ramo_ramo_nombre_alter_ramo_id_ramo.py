# Generated by Django 5.0.6 on 2024-05-31 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_alter_ramo_creditos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ramo',
            old_name='nombre_ramo',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='ramo',
            name='id_ramo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

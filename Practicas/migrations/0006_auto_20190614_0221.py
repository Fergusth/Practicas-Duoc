# Generated by Django 2.1.4 on 2019-06-14 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Practicas', '0005_auto_20190614_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro_practica',
            name='nombre_empresa',
            field=models.CharField(default=111, max_length=50, verbose_name='nombre empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='usuarios_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Practicas.Usuarios'),
        ),
        migrations.AlterField(
            model_name='centro_practica',
            name='rut',
            field=models.CharField(max_length=50, verbose_name='rut'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='usuarios_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Practicas.Usuarios'),
        ),
        migrations.AlterField(
            model_name='supervisor_practica',
            name='usuarios_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Practicas.Usuarios'),
        ),
    ]

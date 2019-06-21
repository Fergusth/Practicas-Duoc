# Generated by Django 2.1.4 on 2019-06-21 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Practicas', '0010_auto_20190621_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='usuarios_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Practicas.Usuarios'),
        ),
        migrations.AlterField(
            model_name='asignatura_alumno',
            name='asignatura_inscrita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Practicas.Asignatura_inscrita', verbose_name='Asignatura'),
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

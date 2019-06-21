# Generated by Django 2.1.4 on 2019-06-21 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Practicas', '0011_auto_20190621_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario_practica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='fecha inicio')),
            ],
            options={
                'verbose_name': 'Formulario_de_practica',
                'verbose_name_plural': 'Formularios_de_practica',
            },
        ),
        migrations.AlterField(
            model_name='alumno',
            name='usuarios_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Practicas.Usuarios'),
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
        migrations.AddField(
            model_name='formulario_practica',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Practicas.Alumno', verbose_name='alumno'),
        ),
        migrations.AddField(
            model_name='formulario_practica',
            name='centro_practica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Practicas.Centro_practica', verbose_name='centro de practica'),
        ),
    ]

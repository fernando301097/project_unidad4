# Generated by Django 4.1.4 on 2022-12-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('tags', models.CharField(max_length=100)),
                ('url_github', models.URLField()),
            ],
        ),
    ]

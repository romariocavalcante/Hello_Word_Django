# Generated by Django 2.0.7 on 2018-08-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='descricao',
            field=models.TextField(max_length=1000),
        ),
    ]

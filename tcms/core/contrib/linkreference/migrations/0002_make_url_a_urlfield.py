# Generated by Django 2.0 on 2017-12-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkreference', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkreference',
            name='url',
            field=models.URLField(),
        ),
    ]

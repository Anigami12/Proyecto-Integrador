# Generated by Django 2.2.4 on 2019-11-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20191124_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='compañia',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 2.2.4 on 2019-11-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria_producto',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
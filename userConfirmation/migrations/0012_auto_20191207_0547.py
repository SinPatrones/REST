# Generated by Django 2.2.7 on 2019-12-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userConfirmation', '0011_auto_20191207_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='codigo',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]

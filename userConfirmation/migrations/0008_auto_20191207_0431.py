# Generated by Django 2.2.7 on 2019-12-07 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userConfirmation', '0007_auto_20191204_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarCode',
            fields=[
                ('codigo', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='inventario',
            name='codigo_barcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userConfirmation.BarCode'),
        ),
    ]
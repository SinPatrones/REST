# Generated by Django 2.2.6 on 2019-10-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userConfirmation', '0002_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='none/no-img.jpg', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadImage',
        ),
    ]
# Generated by Django 4.1.7 on 2023-06-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='no image', upload_to='../Images'),
        ),
    ]

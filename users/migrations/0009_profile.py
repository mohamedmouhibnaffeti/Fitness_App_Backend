# Generated by Django 4.1.7 on 2023-06-18 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='', max_length=50)),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('interactions', models.IntegerField(default=0)),
                ('biography', models.CharField(default='', max_length=80)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
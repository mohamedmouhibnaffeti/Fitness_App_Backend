# Generated by Django 4.1.7 on 2023-06-18 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_reply_related_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='related_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.reply'),
        ),
    ]

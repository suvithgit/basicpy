# Generated by Django 4.2.9 on 2024-01-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-12-31'),
            preserve_default=False,
        ),
    ]
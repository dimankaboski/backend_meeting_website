# Generated by Django 3.2.9 on 2022-03-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1, verbose_name='Пол'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220327_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to='profiles', verbose_name='Фото'),
        ),
    ]

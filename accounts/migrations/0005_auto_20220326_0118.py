# Generated by Django 3.2.9 on 2022-03-25 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220326_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]
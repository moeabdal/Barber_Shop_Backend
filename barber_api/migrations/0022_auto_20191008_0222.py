# Generated by Django 2.2.6 on 2019-10-08 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_api', '0021_auto_20191007_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='services',
            field=models.ManyToManyField(related_name='services', to='barber_api.Service'),
        ),
    ]
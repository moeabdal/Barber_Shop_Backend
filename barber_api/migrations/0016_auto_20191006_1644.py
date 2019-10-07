# Generated by Django 2.2.6 on 2019-10-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
        ('barber_api', '0015_auto_20191003_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_appointments', to='user_api.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='barber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barber_appointments', to='barber_api.Barber'),
        ),
    ]

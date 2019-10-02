# Generated by Django 2.2.6 on 2019-10-02 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barber_api', '0006_auto_20191001_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='credit',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='barber_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='barber_credit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_credit',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='barber_profile_credit', to='barber_api.Credit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='services',
            field=models.ManyToManyField(to='barber_api.Service'),
        ),
    ]

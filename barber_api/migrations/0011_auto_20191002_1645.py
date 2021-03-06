# Generated by Django 2.2.6 on 2019-10-02 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barber_api', '0010_profile_nationality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('experience', models.IntegerField(default=0)),
                ('nationality', models.CharField(max_length=100)),
                ('credit', models.IntegerField(default=0)),
                ('services', models.ManyToManyField(to='barber_api.Service')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='barber_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='services',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Credit',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

# Generated by Django 3.2.23 on 2023-11-20 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0002_alter_artist_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0001_initial'),
        ('subscribeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='A_Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A_subscripton', to='artistapp.artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A_subscripton', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'artist')},
            },
        ),
        migrations.CreateModel(
            name='P_Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_subscripton', to='projectapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_subscripton', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'project')},
            },
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]

# Generated by Django 3.2.23 on 2023-11-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0002_alter_artist_image'),
        ('articleapp', '0003_article_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='artistapp.artist'),
        ),
    ]

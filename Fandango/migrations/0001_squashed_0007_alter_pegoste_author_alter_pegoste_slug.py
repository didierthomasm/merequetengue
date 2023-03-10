# Generated by Django 4.1.7 on 2023-03-06 01:06

import Fandango.models
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('Fandango', '0001_initial'), ('Fandango', '0002_pegoste_image_alter_pegoste_publish_date_and_more'), ('Fandango', '0003_alter_pegoste_author_alter_pegoste_image'), ('Fandango', '0004_pegoste_slug'), ('Fandango', '0005_alter_pegoste_slug'), ('Fandango', '0006_alter_pegoste_slug'), ('Fandango', '0007_alter_pegoste_author_alter_pegoste_slug')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pegoste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(blank=True, max_length=100)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(editable=False, on_delete=models.SET(Fandango.models.get_default_user), to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, upload_to=Fandango.models.get_image_path)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'Pegostes',
            },
        ),
    ]

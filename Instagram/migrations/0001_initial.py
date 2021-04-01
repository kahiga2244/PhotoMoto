# Generated by Django 3.1.7 on 2021-04-01 07:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilephoto', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profilesss')),
                ('Bio', models.CharField(max_length=30)),
                ('following', models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('imageName', models.CharField(blank=True, max_length=30)),
                ('imageCaption', models.CharField(max_length=300)),
                ('comments', models.CharField(blank=True, max_length=30)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Followwww',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('postt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.image')),
                ('userr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.profile')),
            ],
        ),
    ]

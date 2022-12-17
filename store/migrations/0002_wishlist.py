# Generated by Django 4.1.3 on 2022-12-17 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('author', models.CharField(max_length=25)),
                ('genre', models.CharField(max_length=25)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
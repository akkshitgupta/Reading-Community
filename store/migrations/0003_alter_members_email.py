# Generated by Django 4.1.3 on 2022-12-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='eMail',
            field=models.CharField(max_length=14),
        ),
    ]
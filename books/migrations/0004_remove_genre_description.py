# Generated by Django 4.0.4 on 2022-04-29 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_author_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
    ]

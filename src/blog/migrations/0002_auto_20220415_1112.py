# Generated by Django 2.0.7 on 2022-04-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='content',
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-07 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210908_0150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='ticle_image',
            new_name='article_image',
        ),
    ]
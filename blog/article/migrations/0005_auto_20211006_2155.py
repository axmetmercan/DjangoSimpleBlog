# Generated by Django 3.2.7 on 2021-10-06 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]

# Generated by Django 3.2 on 2021-04-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_comment_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='blog',
        ),
    ]

# Generated by Django 3.2 on 2021-04-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_article_comment_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=str),
            preserve_default=False,
        ),
    ]

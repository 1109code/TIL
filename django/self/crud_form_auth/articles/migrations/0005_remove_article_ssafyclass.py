# Generated by Django 4.1 on 2022-09-08 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_ssafyclass_article_ssafyclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='ssafyclass',
        ),
    ]
# Generated by Django 2.2.7 on 2020-02-12 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['-project_created_date']},
        ),
    ]

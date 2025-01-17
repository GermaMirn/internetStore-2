# Generated by Django 5.1 on 2024-09-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_commentheart_options_alter_reviewheart_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='comments/'),
        ),
        migrations.AddField(
            model_name='review',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/'),
        ),
    ]

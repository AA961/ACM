# Generated by Django 4.1.3 on 2022-11-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_rename_cato_slug_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='video_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='videos',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_remove_category_description_videos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='slug',
            new_name='cato_slug',
        ),
        migrations.AlterField(
            model_name='videos',
            name='date',
            field=models.DateField(),
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='videos',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

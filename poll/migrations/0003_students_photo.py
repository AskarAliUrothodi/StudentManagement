# Generated by Django 5.0.3 on 2024-09-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='photo',
            field=models.ImageField(default=2, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]

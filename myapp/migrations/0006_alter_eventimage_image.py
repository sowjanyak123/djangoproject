# Generated by Django 5.0.7 on 2024-07-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_eventimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(upload_to='events/'),
        ),
    ]

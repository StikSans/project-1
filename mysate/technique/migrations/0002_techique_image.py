# Generated by Django 5.1.1 on 2024-09-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='techique',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

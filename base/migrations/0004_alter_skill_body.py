# Generated by Django 5.0.3 on 2024-03-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]

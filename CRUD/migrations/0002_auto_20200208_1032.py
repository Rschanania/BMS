# Generated by Django 3.0 on 2020-02-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='CRUD/'),
        ),
    ]

# Generated by Django 5.1 on 2024-08-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bistroapp', '0002_chef'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chef/'),
        ),
    ]

# Generated by Django 5.1 on 2024-09-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bistroapp', '0007_user_alter_chef_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chef',
            old_name='image',
            new_name='chefimg',
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='menu/'),
        ),
    ]

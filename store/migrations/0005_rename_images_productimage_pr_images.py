# Generated by Django 4.2.2 on 2023-06-18 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='images',
            new_name='pr_images',
        ),
    ]

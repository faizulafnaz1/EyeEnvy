# Generated by Django 4.2.2 on 2023-06-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_desc',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
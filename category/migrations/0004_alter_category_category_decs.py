# Generated by Django 4.2.2 on 2023-06-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_decs',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-30 06:36

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_crop',
            field=image_cropping.fields.ImageRatioField('images', '200x200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image crop'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=image_cropping.fields.ImageCropField(upload_to='photos/categories'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=20),
        ),
    ]

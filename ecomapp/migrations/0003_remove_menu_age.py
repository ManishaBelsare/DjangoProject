# Generated by Django 5.0.7 on 2024-07-24 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_menu_alter_cart_pid_alter_order_pid_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='age',
        ),
    ]

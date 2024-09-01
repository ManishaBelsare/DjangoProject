# Generated by Django 5.0.7 on 2024-07-24 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Menu Name')),
                ('price', models.FloatField()),
                ('age', models.IntegerField()),
                ('cat', models.IntegerField(choices=[(1, 'Maharashtrian Dishes'), (2, 'SouthIndian Dishes'), (3, 'Gujarati Dishes'), (4, 'Chinese Dishes'), (5, 'Sweets'), (6, 'Non-veg Foods')], verbose_name='Category')),
                ('pdetail', models.CharField(max_length=300, verbose_name='Menu Details')),
                ('is_active', models.BooleanField(default=True)),
                ('pimage', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='pid',
            field=models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.CASCADE, to='ecomapp.menu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pid',
            field=models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.CASCADE, to='ecomapp.menu'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

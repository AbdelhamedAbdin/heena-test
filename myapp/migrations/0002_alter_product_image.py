# Generated by Django 4.0.3 on 2022-03-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='https://i2.wp.com/360digital.lk/wp-content/uploads/2020/08/360digital-logo-2.png?fit=1454%2C692&ssl=1', null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2 on 2023-05-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dabbawala', '0004_alter_product_items_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='items_img',
            field=models.ImageField(upload_to='food_items'),
        ),
    ]
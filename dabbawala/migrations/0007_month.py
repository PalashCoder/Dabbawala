# Generated by Django 4.2 on 2023-05-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dabbawala', '0006_product_item_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=20)),
            ],
        ),
    ]

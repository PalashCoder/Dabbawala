# Generated by Django 4.2 on 2023-05-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dabbawala', '0008_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_name', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='best_before',
            field=models.DateField(),
        ),
    ]
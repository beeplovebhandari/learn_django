# Generated by Django 4.2.5 on 2023-09-20 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tables.item')),
            ],
        ),
    ]

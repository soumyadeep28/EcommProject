# Generated by Django 2.2 on 2022-01-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=200)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2022-03-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
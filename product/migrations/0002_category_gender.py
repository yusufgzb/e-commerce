# Generated by Django 3.2.7 on 2022-03-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('man', 'Erkek'), ('woman', 'Kadin'), ('unisex', 'Unisex')], default='unisex', max_length=6),
        ),
    ]

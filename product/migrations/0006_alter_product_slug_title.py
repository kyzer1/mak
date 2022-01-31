# Generated by Django 4.0.1 on 2022-01-31 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_slug_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_title',
            field=models.SlugField(allow_unicode=True, blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

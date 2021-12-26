# Generated by Django 3.2.9 on 2021-12-25 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_sub_category_categoryproduct_parent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.categoryproduct'),
        ),
        migrations.AlterField(
            model_name='categoryproduct',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.categoryproduct'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-10 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salesman_profile', '0010_delete_salesmanproduct'),
        ('product', '0011_remove_product_salesman'),
        ('supply', '0005_rename_product_salesmanproperty_salesman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesmanproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='product.product'),
        ),
        migrations.AlterField(
            model_name='salesmanproduct',
            name='salesman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesmans', to='salesman_profile.salesmanprofile'),
        ),
    ]

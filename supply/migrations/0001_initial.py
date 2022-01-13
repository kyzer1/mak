# Generated by Django 4.0 on 2022-01-12 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('salesman_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesmanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=True)),
                ('date_import_product', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_last_update', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.BigIntegerField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='product.product')),
                ('salesman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesmans', to='salesman_profile.salesmanprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SalesManProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('prop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='props', to='product.property')),
                ('salesman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesproducts', to='supply.salesmanproduct')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-26 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cart_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryCustomer',
            fields=[
                ('cart_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cart.cart')),
            ],
            bases=('cart.cart',),
        ),
    ]
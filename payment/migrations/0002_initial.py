# Generated by Django 4.0 on 2022-01-09 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salesman_profile', '0001_initial'),
        ('payment', '0001_initial'),
        ('customer_profile', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer_profile.customerprofile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='salesman_profile.salesmanprofile'),
        ),
    ]

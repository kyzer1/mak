# Generated by Django 4.0 on 2021-12-18 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0002_initial'),
        ('salesman_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='userseller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salesman_profile.salesmanprofile'),
        ),
    ]

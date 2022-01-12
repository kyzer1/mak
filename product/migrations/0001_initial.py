# Generated by Django 4.0 on 2022-01-12 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_cat', to='product.categoryproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop', models.CharField(max_length=255, verbose_name='properties')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='product.categoryproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('img1', models.ImageField(blank=True, null=True, upload_to='product_media/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='product_media/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='product_media/')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='product_media/')),
                ('active', models.BooleanField(default=True)),
                ('date_prodcut', models.DateTimeField(auto_now=True)),
                ('sold_out_num', models.BigIntegerField(blank=True, null=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.categoryproduct')),
            ],
        ),
    ]

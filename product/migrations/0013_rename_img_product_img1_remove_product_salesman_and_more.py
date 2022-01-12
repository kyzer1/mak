# Generated by Django 4.0 on 2022-01-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_sold_out_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='img1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='salesman',
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='product_media/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='product_media/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='product_media/'),
        ),
        migrations.AlterField(
            model_name='categoryproduct',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_cat', to='product.categoryproduct'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.categoryproduct'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='product.categoryproduct'),
        ),
    ]
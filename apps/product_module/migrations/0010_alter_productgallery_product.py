# Generated by Django 4.2 on 2023-06-06 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_productgallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='product_module.product', verbose_name='محصول'),
        ),
    ]
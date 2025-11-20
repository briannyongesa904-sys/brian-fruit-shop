from django.db import migrations
import json
import os

def load_products(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    fixture_path = os.path.join(os.path.dirname(__file__), '../fixtures/products.json')
    with open(fixture_path, encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            fields = item['fields']
            Product.objects.update_or_create(
                id=item['pk'],
                defaults=fields
            )

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_unit_alter_product_price'),  # replace 0001_initial with your last migration
    ]

    operations = [
        migrations.RunPython(load_products),
    ]

    ]

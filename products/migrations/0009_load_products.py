from django.db import migrations
import json
import os

def load_products(apps, schema_editor):
    Product = apps.get_model('products', 'Product')

    # Path to the fixtures folder
    fixture_path = os.path.join(os.path.dirname(__file__), '../fixtures/products_fixed.json')

    # Use utf-8-sig to handle possible BOM in the JSON file
    with open(fixture_path, encoding='utf-8-sig') as f:
        data = json.load(f)
        for item in data:
            fields = item['fields']
            Product.objects.update_or_create(
                id=item['pk'],
                defaults=fields
            )

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_unit_alter_product_price'),
    ]

    operations = [
        migrations.RunPython(load_products),
    ]

# Generated by Django 3.2 on 2022-01-22 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('silq', '0011_po_summary_style_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='po_summary',
            old_name='project_estimated_delivery',
            new_name='project_estimated_delivery_date',
        ),
    ]

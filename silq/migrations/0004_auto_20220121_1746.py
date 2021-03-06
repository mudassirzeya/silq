# Generated by Django 3.2 on 2022-01-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silq', '0003_auto_20220121_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_of_materials',
            name='criticality',
            field=models.CharField(blank=True, choices=[('Critical', 'Critical'), ('Minor', 'Minor'), ('Major', 'Major')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bill_of_materials',
            name='item_style',
            field=models.CharField(blank=True, choices=[('Fabric', 'Fabric'), ('Thread', 'Thread'), ('Button', 'Button'), ('Interfacing', 'Interfacing'), ('Nect Tape', 'Nect Tape'), ('Zipper', 'Zipper'), ('Jaquard Label', 'Jaquard Label'), ('Bottom Tape', 'Bottom Tape'), ('Embroidery', 'Embroidery'), ('Buckle', 'Buckle'), ('Aglets', 'Aglets'), ('Heel', 'Heel'), ('Toplift', 'Toplift'), ('Foam Padding', 'Foam Padding'), ('Socks', 'Socks'), ('Elastic', 'Elastic')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='measurement_chart',
            name='criticality',
            field=models.CharField(blank=True, choices=[('Critical', 'Critical'), ('Minor', 'Minor'), ('Major', 'Major')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='other_issue',
            name='criticality',
            field=models.CharField(blank=True, choices=[('Critical', 'Critical'), ('Minor', 'Minor'), ('Major', 'Major')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='other_issue',
            name='section',
            field=models.CharField(blank=True, choices=[('Construction', 'Construction'), ('Stitching', 'Stitching')], max_length=500, null=True),
        ),
    ]

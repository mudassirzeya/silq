# Generated by Django 3.2 on 2022-01-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_note',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
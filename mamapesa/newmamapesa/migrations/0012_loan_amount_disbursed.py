# Generated by Django 5.0.2 on 2024-03-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newmamapesa', '0011_merge_20240301_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='amount_disbursed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

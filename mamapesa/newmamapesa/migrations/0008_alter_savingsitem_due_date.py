# Generated by Django 5.0.2 on 2024-02-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newmamapesa', '0007_remove_savings_end_date_remove_savings_in_progress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingsitem',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]

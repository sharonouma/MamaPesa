# Generated by Django 5.0.2 on 2024-03-01 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newmamapesa', '0013_alter_loan_duration_months'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to=settings.AUTH_USER_MODEL),
        ),
    ]

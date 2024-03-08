# Generated by Django 5.0.2 on 2024-03-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('newmamapesa', '0007_remove_loan_purpose_alter_loantransaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='idnumber',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='interest_rate',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='loan_limit',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='loan_owed',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, default='replace@gmail.com', max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterModelTable(
            name='loan',
            table='Loans',
        ),
    ]

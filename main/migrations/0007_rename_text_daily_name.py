# Generated by Django 4.0.6 on 2022-08-05 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_daily_name_daily_complete_daily_due_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily',
            old_name='text',
            new_name='name',
        ),
    ]

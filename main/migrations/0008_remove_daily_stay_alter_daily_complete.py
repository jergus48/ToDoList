# Generated by Django 4.0.6 on 2022-08-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_text_daily_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily',
            name='stay',
        ),
        migrations.AlterField(
            model_name='daily',
            name='complete',
            field=models.BooleanField(),
        ),
    ]

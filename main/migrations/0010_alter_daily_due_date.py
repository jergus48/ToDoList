# Generated by Django 4.0.6 on 2022-10-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_daily_user_todolist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='due_date',
            field=models.TimeField(null=True),
        ),
    ]

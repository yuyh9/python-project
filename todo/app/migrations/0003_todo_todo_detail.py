# Generated by Django 4.2.2 on 2023-06-13 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_data_todo_date_alter_todo_priority_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_detail',
            field=models.TextField(blank=True),
        ),
    ]

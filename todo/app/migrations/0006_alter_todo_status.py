# Generated by Django 4.2.2 on 2023-06-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_todo_todo_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'Complete'), ('P', 'Pending')], max_length=2),
        ),
    ]

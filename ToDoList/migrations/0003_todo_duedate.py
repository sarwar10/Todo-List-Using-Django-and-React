# Generated by Django 4.1.1 on 2023-01-16 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0002_rename_status_todo_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
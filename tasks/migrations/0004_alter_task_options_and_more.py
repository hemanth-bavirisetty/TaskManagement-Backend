# Generated by Django 5.1.3 on 2024-11-22 04:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['user', 'status'], name='tasks_task_user_id_c0fce1_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['deadline'], name='tasks_task_deadlin_736196_idx'),
        ),
    ]

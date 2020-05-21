# Generated by Django 3.0.5 on 2020-05-21 11:29

import datetime
from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import User
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0005_document_permission_whiteboard_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='change_task',
            name='creation_user',
            field=models.ForeignKey(default=User.objects.get(pk=1).id, on_delete=django.db.models.deletion.CASCADE, related_name='change_task_creation_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kanban_board',
            name='creation_user',
            field=models.ForeignKey(default=User.objects.get(pk=1).id, on_delete=django.db.models.deletion.CASCADE, related_name='kanban_board_creation_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='creation_user',
            field=models.ForeignKey(default=User.objects.get(pk=1).id, on_delete=django.db.models.deletion.CASCADE, related_name='project_creation_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='creation_user',
            field=models.ForeignKey(default=User.objects.get(pk=1).id, on_delete=django.db.models.deletion.CASCADE, related_name='quote_creation_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requirement',
            name='creation_user',
            field=models.ForeignKey(default=User.objects.get(pk=1).id, on_delete=django.db.models.deletion.CASCADE, related_name='requirement_creation_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='creation_user',
            field=models.ForeignKey(default=User.objects.get(pk=1).id, on_delete=django.db.models.deletion.CASCADE, related_name='task_creation_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

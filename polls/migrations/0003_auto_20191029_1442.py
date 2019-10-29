# Generated by Django 2.2.6 on 2019-10-29 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_responses_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='responses',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responses',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

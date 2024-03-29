# Generated by Django 4.2 on 2023-06-25 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_compatibility_incompatible_with_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperature',
            name='optimal_temperature',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='plant',
        ),
        migrations.AddField(
            model_name='temperature',
            name='temperature',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperature',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2 on 2023-06-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_plant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreenhouse',
            name='cell',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

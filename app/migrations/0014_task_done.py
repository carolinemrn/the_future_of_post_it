# Generated by Django 3.0.2 on 2020-02-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200131_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]

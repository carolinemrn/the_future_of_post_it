# Generated by Django 3.0.2 on 2020-01-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200130_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='postit',
            name='tasks',
            field=models.ManyToManyField(to='app.Task'),
        ),
        migrations.DeleteModel(
            name='PostItTask',
        ),
    ]
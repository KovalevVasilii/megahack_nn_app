# Generated by Django 2.2 on 2019-04-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='table',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
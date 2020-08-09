# Generated by Django 3.0.8 on 2020-08-09 08:50

from django.db import migrations, models
import urlsApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entry_id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.TextField(max_length=1000)),
                ('path', models.CharField(default=urlsApp.models.random_path, max_length=1000)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
    ]

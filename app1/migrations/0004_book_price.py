# Generated by Django 2.2.1 on 2019-06-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]

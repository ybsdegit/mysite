# Generated by Django 2.2.1 on 2019-06-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('books', models.ManyToManyField(to='app1.Book')),
            ],
        ),
    ]

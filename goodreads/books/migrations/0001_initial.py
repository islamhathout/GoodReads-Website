# Generated by Django 2.0.2 on 2018-02-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_category', models.CharField(max_length=50)),
                ('book_description', models.CharField(max_length=1000)),
                ('Book_cover', models.CharField(max_length=1000)),
            ],
        ),
    ]
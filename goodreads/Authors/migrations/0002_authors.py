# Generated by Django 2.0.2 on 2018-03-10 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author_Name', models.CharField(max_length=100)),
                ('Author_DoB', models.DateField(blank=True, null=True)),
                ('Author_Bio', models.CharField(max_length=200)),
                ('author_img', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2024-02-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('email', models.EmailField(max_length=250, verbose_name='Student Email')),
            ],
        ),
    ]

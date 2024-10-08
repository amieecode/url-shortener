# Generated by Django 5.1 on 2024-08-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=256)),
                ('hashing', models.CharField(max_length=10, unique=True)),
                ('creation_date', models.DateTimeField(verbose_name='creation_date')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

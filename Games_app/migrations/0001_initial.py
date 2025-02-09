# Generated by Django 5.1.4 on 2025-01-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('developers_company', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('mark', models.IntegerField()),
                ('price_usd', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-02-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_company', models.CharField(max_length=50, unique=True)),
                ('mobile_name', models.CharField(max_length=50)),
                ('mobile_spec', models.TextField()),
                ('mobile_price', models.IntegerField(default=1000)),
            ],
        ),
    ]

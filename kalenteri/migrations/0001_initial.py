# Generated by Django 4.1.6 on 2023-03-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tapahtuma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=100)),
                ('lisätietoja', models.CharField(max_length=200)),
                ('alku', models.DateTimeField()),
                ('loppu', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]



from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelmasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='ohjelma',
            name='kategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ohjelma.kategoria'),
        ),
    ]
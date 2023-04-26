

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelmasi', '0002_kategoria_ohjelmasi_kategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='ohjelmasi',
            name='merkattu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ohjelmasi.kategoria'),
        
        ),    
    ]

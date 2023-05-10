from django.db import migrations, models

class Migrations(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
        name = "kalenteri",
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID' )),

            ('tapahtuma_kenttä', models.DateTimeField()),
        ],

    ),

]
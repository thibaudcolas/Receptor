# Generated by Django 3.1.7 on 2021-04-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oligos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usage',
            options={'ordering': ['usage']},
        ),
        migrations.AlterField(
            model_name='oligo',
            name='primer_position',
            field=models.CharField(blank=True, choices=[('Sense', 'Sense'), ('Antisense', 'Antisense'), ('Unspecified', 'Unspecified')], default='Unspecified', max_length=12),
        ),
    ]

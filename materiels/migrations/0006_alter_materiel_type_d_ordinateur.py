# Generated by Django 4.2.4 on 2024-04-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiels', '0005_materiel_references'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='type_d_ordinateur',
            field=models.CharField(choices=[('en panne', 'En Panne'), ('en diagnostique', 'En Diagnostique'), ('bon etat', 'Bon État')], default='bon etat', max_length=100),
        ),
    ]

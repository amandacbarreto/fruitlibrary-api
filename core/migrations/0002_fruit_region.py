# Generated by Django 4.0.3 on 2022-03-30 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='region',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='fruits', to='core.region'),
            preserve_default=False,
        ),
    ]

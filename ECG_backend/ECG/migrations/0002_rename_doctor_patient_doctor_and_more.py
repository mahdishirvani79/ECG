# Generated by Django 4.0 on 2021-12-27 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECG', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Doctor',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='Patient',
            new_name='patient',
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_alter_job_vehicle_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="vehicle_size",
            field=models.FloatField(
                blank=True, choices=[(1.0, 1.0), (1.5, 1.5)], default=1.0, null=True
            ),
        ),
    ]
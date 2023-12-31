# Generated by Django 4.2.5 on 2023-10-02 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0006_apply"),
    ]

    operations = [
        migrations.AddField(
            model_name="apply",
            name="job",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="apply_job",
                to="job.job",
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0006_alter_engine_engine_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="engine",
            name="engine_number",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
# Generated by Django 5.1.2 on 2024-11-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_aluno_matricula"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ano",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data", models.CharField(max_length=4)),
            ],
        ),
    ]

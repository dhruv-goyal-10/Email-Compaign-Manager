# Generated by Django 4.2.4 on 2023-08-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campaign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=200)),
                ("preview_text", models.TextField()),
                ("article_url", models.URLField()),
                ("html_content", models.TextField()),
                ("plain_text_content", models.TextField()),
                ("published_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                ("scheduled_time", models.DateTimeField(blank=True, null=True)),
                ("celery_id", models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                "verbose_name": "Campaign",
                "verbose_name_plural": "Campaigns",
            },
        ),
    ]
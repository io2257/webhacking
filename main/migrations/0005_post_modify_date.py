# Generated by Django 4.1.5 on 2023-01-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
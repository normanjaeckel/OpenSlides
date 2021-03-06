# Generated by Django 2.1.5 on 2019-01-19 13:25

from django.conf import settings
from django.db import migrations, models

import openslides.utils.models


class Migration(migrations.Migration):

    dependencies = [("agenda", "0005_auto_20180815_1109")]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=openslides.utils.models.SET_NULL_AND_AUTOUPDATE,
                related_name="children",
                to="agenda.Item",
            ),
        ),
        migrations.AlterField(
            model_name="speaker",
            name="user",
            field=models.ForeignKey(
                on_delete=openslides.utils.models.CASCADE_AND_AUTOUPDATE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

# Generated by Django 3.0.14 on 2021-06-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RV1', '0006_auto_20210603_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='crs_content',
            field=models.CharField(default='', max_length=100000),
            preserve_default=False,
        ),
    ]

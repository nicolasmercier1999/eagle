# Generated by Django 3.0.14 on 2021-06-03 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RV1', '0005_auto_20210603_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='chp_id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='mdl_id',
        ),
        migrations.RemoveField(
            model_name='share_file',
            name='dcm_id',
        ),
        migrations.RemoveField(
            model_name='share_file',
            name='prt_id',
        ),
        migrations.RemoveField(
            model_name='share_file',
            name='usr_id',
        ),
        migrations.RemoveField(
            model_name='share_support',
            name='chp_id',
        ),
        migrations.RemoveField(
            model_name='share_support',
            name='crs_id',
        ),
        migrations.RemoveField(
            model_name='share_support',
            name='dcm_id',
        ),
        migrations.RemoveField(
            model_name='share_support',
            name='mdl_id',
        ),
        migrations.AddField(
            model_name='course',
            name='chp',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Chapter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='mdl',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_file',
            name='dcm',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Document'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_file',
            name='prt',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Permission_Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_file',
            name='usr',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_support',
            name='chp',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Chapter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_support',
            name='crs',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_support',
            name='dcm',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Document'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_support',
            name='mdl',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='RV1.Module'),
            preserve_default=False,
        ),
    ]

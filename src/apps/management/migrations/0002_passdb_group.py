# Generated by Django 4.0 on 2022-07-27 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passdb',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
    ]

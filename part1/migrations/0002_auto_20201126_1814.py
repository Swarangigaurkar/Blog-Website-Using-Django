# Generated by Django 3.1.3 on 2020-11-26 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pusername',
            field=models.ForeignKey(db_column='pusername', on_delete=django.db.models.deletion.CASCADE, to='part1.userinfo', to_field='username'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-07-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_profile', '0002_user_data_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='file',
            field=models.CharField(max_length=264),
        ),
    ]

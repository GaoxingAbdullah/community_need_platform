# Generated by Django 4.1 on 2023-02-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnp', '0002_remove_event_date_event_eventdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

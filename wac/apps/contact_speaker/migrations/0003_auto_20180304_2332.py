# Generated by Django 2.0.1 on 2018-03-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_speaker', '0002_auto_20180304_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='event_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='event_time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

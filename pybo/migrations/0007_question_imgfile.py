# Generated by Django 3.1.3 on 2022-02-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20220215_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.1 on 2020-10-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcv', '0012_auto_20201030_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

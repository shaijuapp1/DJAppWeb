# Generated by Django 5.0.4 on 2024-07-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_appflow_action_by_filed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appfileds',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='appflow',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='appstatus',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]

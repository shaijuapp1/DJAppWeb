# Generated by Django 5.0.4 on 2024-07-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_alter_appfileds_access'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppView',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField(default=0)),
                ('app_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('html', models.TextField()),
                ('js', models.TextField()),
            ],
        ),
    ]

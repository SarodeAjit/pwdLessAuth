# Generated by Django 2.2.3 on 2019-07-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190728_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cqrcode',
            name='id',
        ),
        migrations.AlterField(
            model_name='cqrcode',
            name='uniqueId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.2.4 on 2019-09-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0006_auto_20190905_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sith',
            name='shadowhand',
            field=models.ManyToManyField(related_name='siths', to='recruit.PassedTest'),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_auto_20181219_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='topic',
            field=models.ManyToManyField(blank=True, related_name='categories', to='hello.Topic'),
        ),
    ]

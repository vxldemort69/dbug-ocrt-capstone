# Generated by Django 3.0.7 on 2020-07-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0002_auto_20200707_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='done_requests',
            name='comments',
            field=models.TextField(default='this is a comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pending_requests',
            name='comments',
            field=models.TextField(default='this is a comment'),
            preserve_default=False,
        ),
    ]

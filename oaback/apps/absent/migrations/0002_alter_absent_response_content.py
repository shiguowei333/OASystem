# Generated by Django 5.1.5 on 2025-02-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absent',
            name='response_content',
            field=models.TextField(blank=True, verbose_name='审批意见'),
        ),
    ]

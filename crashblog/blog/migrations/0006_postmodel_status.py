# Generated by Django 5.0.1 on 2024-02-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20190721_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(max_length=120),
        ),
    ]
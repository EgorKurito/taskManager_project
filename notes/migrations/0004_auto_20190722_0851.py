# Generated by Django 2.2.3 on 2019-07-22 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20190722_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(default='Note', on_delete=django.db.models.deletion.CASCADE, to='notes.Category'),
        ),
    ]

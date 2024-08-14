# Generated by Django 5.1 on 2024-08-14 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_contact_description_alter_contact_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='media',
        ),
        migrations.AddField(
            model_name='contact',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='recipes/covers/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agenda.category'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

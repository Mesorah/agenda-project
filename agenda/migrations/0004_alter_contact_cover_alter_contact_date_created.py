# Generated by Django 5.1 on 2024-08-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_remove_contact_media_contact_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cover',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='contact/covers/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
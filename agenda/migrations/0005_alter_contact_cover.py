# Generated by Django 5.1 on 2024-08-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_alter_contact_cover_alter_contact_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='contact/covers/%Y/%m/%d/'),
        ),
    ]
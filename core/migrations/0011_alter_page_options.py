# Generated by Django 3.2.18 on 2023-06-14 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_page_pagepost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Page'},
        ),
    ]

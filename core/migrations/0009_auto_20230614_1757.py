# Generated by Django 3.2.18 on 2023-06-14 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_grouppost_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grouppost',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Group Post'},
        ),
        migrations.RenameField(
            model_name='group',
            old_name='host',
            new_name='user',
        ),
    ]
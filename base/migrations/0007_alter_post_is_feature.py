# Generated by Django 4.0.5 on 2022-07-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_gallery_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_feature',
            field=models.BooleanField(default=True),
        ),
    ]

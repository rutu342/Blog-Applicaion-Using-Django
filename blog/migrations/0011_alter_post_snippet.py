# Generated by Django 4.0.4 on 2022-06-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
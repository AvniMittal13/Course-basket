# Generated by Django 4.0.2 on 2022-02-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_course_ltpc'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(default=0),
        ),
    ]
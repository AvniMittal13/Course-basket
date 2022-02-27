# Generated by Django 4.0.2 on 2022-02-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_course_credits'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('DSE', 'DSE'), ('ME', 'ME'), ('EE', 'EE'), ('CE', 'CE'), ('BioE', 'BioE')], default='CSE', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='completed_courses',
            field=models.ManyToManyField(blank=True, related_name='completed_courses', to='home.Course'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rollno',
            field=models.CharField(default='Not updated', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='sem',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], default='1st', max_length=30),
        ),
    ]

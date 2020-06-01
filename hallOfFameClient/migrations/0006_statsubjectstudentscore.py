# Generated by Django 3.0.5 on 2020-05-08 16:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hallOfFameClient', '0005_auto_20200508_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatSubjectStudentScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mean_value', models.FloatField()),
                ('stat_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stat_students_score', to='hallOfFameClient.StatSubjectScore')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stat_subjects_score', to='hallOfFameClient.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-07 18:53

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import hallOfFameClient.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_score', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('etcs', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('album_number', models.IntegerField(unique=True, validators=[hallOfFameClient.validators.validate_album_number])),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='hallOfFameClient.Semester')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('etcs', models.SmallIntegerField()),
                ('lecturers', models.ManyToManyField(related_name='subjects', to='hallOfFameClient.Lecturer')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='hallOfFameClient.Semester')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='hallOfFameClient.Exercise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='hallOfFameClient.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('lecturers', models.ManyToManyField(related_name='groups', to='hallOfFameClient.Lecturer')),
                ('students', models.ManyToManyField(related_name='groups', to='hallOfFameClient.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='hallOfFameClient.Subject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='hallOfFameClient.Group'),
        ),
    ]

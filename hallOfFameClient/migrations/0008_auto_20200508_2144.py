# Generated by Django 3.0.5 on 2020-05-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hallOfFameClient', '0007_auto_20200508_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='statgroupscore',
            name='date',
        ),
        migrations.RemoveField(
            model_name='statgroupstudentscore',
            name='date',
        ),
        migrations.RemoveField(
            model_name='statsubjectscore',
            name='date',
        ),
        migrations.RemoveField(
            model_name='statsubjectstudentscore',
            name='date',
        ),
    ]

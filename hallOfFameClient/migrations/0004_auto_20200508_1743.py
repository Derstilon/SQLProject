# Generated by Django 3.0.5 on 2020-05-08 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hallOfFameClient', '0003_auto_20200508_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statgroupscore',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stat_score', to='hallOfFameClient.Group'),
        ),
        migrations.AlterField(
            model_name='statgroupstudentscore',
            name='stat_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stat_students_score', to='hallOfFameClient.StatGroupScore'),
        ),
        migrations.AlterField(
            model_name='statgroupstudentscore',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stat_groups_score', to='hallOfFameClient.Student'),
        ),
        migrations.AlterField(
            model_name='statsubjectscore',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stat_score', to='hallOfFameClient.Subject'),
        ),
    ]

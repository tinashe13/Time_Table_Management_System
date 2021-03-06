# Generated by Django 2.2 on 2019-04-15 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_teacher_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time_Slot', models.CharField(choices=[('1', '9:00-10:00'), ('2', '10:00-11:00'), ('3', '11:00-12:00'), ('4', '12:00-1:00'), ('5', '2:00-3:00'), ('6', '3:00-4:00'), ('7', '4:00-5:00')], default='1', max_length=1)),
                ('Day', models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday')], default='1', max_length=1)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Course')),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Teacher')),
                ('Venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Venue')),
            ],
        ),
    ]

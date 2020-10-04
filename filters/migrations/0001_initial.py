# Generated by Django 3.1 on 2020-10-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True, max_length=250)),
                ('question_type', models.CharField(choices=[('select', 'select'), ('task', 'task'), ('problem', 'problem'), ('question', 'question')], default='select', max_length=25)),
                ('ticket_priority', models.CharField(choices=[('high', 'high'), ('low', 'low'), ('medium', 'medium')], default=None, max_length=25)),
            ],
        ),
    ]

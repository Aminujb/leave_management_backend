# Generated by Django 3.1.5 on 2021-01-21 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('leave_type', models.CharField(max_length=20)),
                ('note', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Leaves', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_applied'],
            },
        ),
    ]

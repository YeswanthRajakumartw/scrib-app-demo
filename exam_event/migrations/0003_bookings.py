# Generated by Django 4.2.1 on 2023-06-04 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam_event', '0002_alter_exam_tickets_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_event.exam')),
                ('exam_attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_attendee_events', to=settings.AUTH_USER_MODEL)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
from django.db import models
from datetime import datetime, timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        leaved_at = self.leaved_at if self.leaved_at else datetime.now(timezone.min)
        return leaved_at - self.entered_at

    def format_duration(self, duration):
        hours, reminder = divmod(duration.total_seconds(), 3600)
        minutes, _ = divmod(reminder, 60)
        return '{:}:{:02d}'.format(int(hours), int(minutes))

    def is_visit_long(self, minutes=60):
        return self.get_duration().total_seconds() > minutes * 60

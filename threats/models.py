from django.conf import settings
from django.db import models


class Pillar(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class AttackTechnique(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    pillar = models.ForeignKey(Pillar, on_delete=models.CASCADE, related_name="techniques")

    def __str__(self):
        return self.name


class Finding(models.Model):
    class Severity(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"
        CRITICAL = "CRITICAL", "Critical"

    class Status(models.TextChoices):
        OPEN = "OPEN", "Open"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        RESOLVED = "RESOLVED", "Resolved"

    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=Severity.choices, default=Severity.MEDIUM)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.OPEN)
    date_logged = models.DateTimeField(auto_now_add=True)
    technique = models.ForeignKey(AttackTechnique, on_delete=models.PROTECT, related_name="findings")
    logged_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="findings")

    def update_status(self, new_status):
        if new_status not in self.Status.values:
            raise ValueError("Invalid status")
        self.status = new_status
        self.save()

    def __str__(self):
        return self.title


class Mitigation(models.Model):
    finding = models.ForeignKey(Finding, on_delete=models.CASCADE, related_name="mitigations")
    action_taken = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)
    outcome = models.CharField(max_length=200, blank=True)
    applied_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="mitigations")

    def __str__(self):
        return f"Mitigation for {self.finding}"
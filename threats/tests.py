from django.test import TestCase

from accounts.models import User
from .models import AttackTechnique, Finding, Pillar


class FindingStatusTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester1", password="StrongPass#123", role=User.Role.TESTER
        )
        pillar = Pillar.objects.create(name="CI/CD")
        technique = AttackTechnique.objects.create(name="Pipeline poisoning", pillar=pillar)
        self.finding = Finding.objects.create(
            title="Poisoned build step",
            description="Unreviewed script added to the build workflow.",
            severity=Finding.Severity.HIGH,
            technique=technique,
            logged_by=self.user,
        )

    def test_update_status_changes_status(self):
        self.assertEqual(self.finding.status, Finding.Status.OPEN)
        self.finding.update_status(Finding.Status.RESOLVED)
        self.finding.refresh_from_db()
        self.assertEqual(self.finding.status, Finding.Status.RESOLVED)
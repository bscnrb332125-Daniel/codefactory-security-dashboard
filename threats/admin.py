from django.contrib import admin

from .models import AttackTechnique, Finding, Mitigation, Pillar

admin.site.register(Pillar)
admin.site.register(AttackTechnique)
admin.site.register(Finding)
admin.site.register(Mitigation)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from analytics_dashboard.core.models import User


class AnalyticsDashboardUserAdmin(UserAdmin):
    pass


admin.site.register(User, AnalyticsDashboardUserAdmin)

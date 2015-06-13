from django.contrib import admin

from .models import Account, Alert, DailyAccountMetrics, Campaign, DailyCampaignMetrics, AdGroup, DailyAdGroupMetrics, Ad, DailyAdMetrics, ReportFile

admin.site.register(Account)
admin.site.register(Alert)
admin.site.register(DailyAccountMetrics)
admin.site.register(Campaign)
admin.site.register(DailyCampaignMetrics)
admin.site.register(AdGroup)
admin.site.register(DailyAdGroupMetrics)
admin.site.register(Ad)
admin.site.register(DailyAdMetrics)
admin.site.register(ReportFile)
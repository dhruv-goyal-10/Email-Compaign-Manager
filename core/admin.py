from django.contrib import admin
from core.models import Campaign
# Register your models here.

class CampaignAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'subject', 'preview_text', 'article_url', 'html_content', 'plain_text_content')
    list_display_links = ('id', 'subject')
    search_fields = ('subject', 'preview_text', 'article_url', 'html_content', 'plain_text_content')
    list_per_page = 25

admin.site.register(Campaign, CampaignAdmin)
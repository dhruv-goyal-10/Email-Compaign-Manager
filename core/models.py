from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from project.celery import app
from core.task import custom_mail


class Campaign(models.Model):
    
    subject = models.CharField(max_length = 200)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateField(auto_now_add = True)
    is_active = models.BooleanField(default = True)
    scheduled_time = models.DateTimeField(blank = True, null = True)
    celery_id = models.CharField(max_length = 200, blank = True, null = True)
    
    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return self.subject
    

@receiver(pre_save, sender = Campaign)
def assign_tasks_to_celery(sender, instance, **kwargs):


    if instance.scheduled_time is not None:
        
        if instance.celery_id is not None:
            app.control.revoke(instance.celery_id)
            
        celery_id = custom_mail.apply_async(args = [instance.subject, 
                                                   instance.preview_text, 
                                                   instance.article_url, 
                                                   instance.html_content, 
                                                   instance.plain_text_content], 
                                           eta = instance.scheduled_time)
        instance.celery_id = celery_id

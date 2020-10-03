from django.db import models
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.

@register_setting
class SocialMediaSettings(BaseSetting):
    '''socail media  setting for website'''
    facebook=models.URLField(blank=True,null=True,help_text='facebook')
    twitter=models.URLField(blank=True,null=True,help_text='twitter')
    youtube=models.URLField(blank=True,null=True,help_text='youtube')

    panels=[
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('youtube'),

        ],heading='SocialMedia links')
    ]
from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page,Orderable
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel,InlinePanel,MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin,route



class HomePageCarouselImages(Orderable):
    '''1 to 5 images for homepage carousel'''
    page=ParentalKey('home.HomePage',related_name='carousel_images')
    carousel_image=models.ForeignKey('wagtailimages.Image',
                                   null=True,
                                   blank=False,
                                   on_delete=models.SET_NULL,
                                   related_name='+')

    panels=[
        ImageChooserPanel('carousel_image'),
    ]


class HomePage(RoutablePageMixin,Page):
    template = 'home/home_page.html'
    max_count = 1

    banner_title=models.CharField(max_length=100,blank=False,null=True)
    banner_subtitle=RichTextField(features=['bold','italic'],)
    banner_image=models.ForeignKey('wagtailimages.Image',
                                   null=True,
                                   blank=False,
                                   on_delete=models.SET_NULL,
                                   related_name='+')
    banner_cta=models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content=StreamField(
        [
         ('cta', blocks.CTABlock()),
         ('card',blocks.CardBlock()),
    ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels+[
        MultiFieldPanel([
            FieldPanel('banner_title'),
            FieldPanel('banner_subtitle'),
            ImageChooserPanel('banner_image'),
            PageChooserPanel('banner_cta'),],
            heading='Banner Options'),
        MultiFieldPanel([InlinePanel('carousel_images',max_num=5,min_num=0,label='Image'), ], heading='Carousel Images'),

        StreamFieldPanel('content'),

    ]

    class Meta:
        verbose_name='Home Page'

    @route(r'^subscribe/$')
    def the_subscribe_page(self,request,*args,**kwargs):
         context=self.get_context(request,*args,**kwargs)
         context['a_special_test']='heello world 123123'
         return render(request,'home/subscribe.html',context)



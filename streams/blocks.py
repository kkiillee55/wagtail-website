'''streamfields used in flex/models.py'''

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock as codeBlock
# from blog import models

class TitleAndTextBlock(blocks.StructBlock):

    title=blocks.CharBlock(required=True,help_text='Add ur title')
    text=blocks.TextBlock(required=True,help_text='Add ur text')

    class Meta:
        template='streams/title_and_text_block.html'
        icon='edit'
        label='Title & Text'


class CardBlock(blocks.StructBlock):
    '''cards with image, text and button'''
    title=blocks.CharBlock(required=True,help_text='Add card title')


    cards=blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image',ImageChooserBlock(requires=True)),
                ('title',blocks.CharBlock(required=True,max_length=40)),
                ('text',blocks.TextBlock(required=True,max_length=200)),
                ('button_page',blocks.PageChooserBlock(required=False)),
                ('button_url',blocks.URLBlock(required=False,help_text='if botton_page is selected, it will be used first')),
            ]
        )
    )
    class Meta:
        template='streams/card_block.html'
        icon='placeholder'
        label='Staff Cards'





class RichtextBlock(blocks.RichTextBlock):
    '''richtextblock with full features'''
    name = 'fullrichtext'
    class Meta:
        template='streams/richtext_block.html'
        icon='doc-full'
        label='Full RichText'


# class CodeBlock(blocks.RichTextBlock):
#     '''richtextblock with full features'''
#     class Meta:
#         template='streams/code_block.html'
#         icon='doc-full'
#         label='Code'
class CodeBlock(blocks.StructBlock):
    '''richtextblock with full features'''
    code=codeBlock(label='Code')
    class Meta:
        template='streams/code_block.html'
        icon='doc-full'


class SimpleRichtextBlock(blocks.RichTextBlock):
    '''richtextblock with limited features'''

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features=['bold','italic','link']


    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Simple RichText'


class CTABlock(blocks.StructBlock):
    '''a smiple call to action section'''
    title=blocks.CharBlock(required=True,max_length=50)
    text=blocks.RichTextBlock(required=True,features=['bold','italic'])

    #internal
    button_page=blocks.PageChooserBlock(required=False)
    #external
    button_url=blocks.URLBlock(required=False)
    button_text=blocks.CharBlock(required=True,default='Learn MOre',max_length=40)

    class Meta:
        template='streams/cta_block.html'
        icon='placeholder'
        label='Call to action'


class LinkStructValue(blocks.StructValue):
    '''additional logic for buttonblock urls'''

    def url(self):
        button_page=self.get('button_page')
        button_url=self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url
        return None

    # def latest_posts(self):
    #
    #     return blog.models.BlogDetailPage.objects.live().public()[:3]



class ButtonBlock(blocks.StructBlock):
    '''extern or intern url'''
    button_page = blocks.PageChooserBlock(required=False,help_text='if selected,used first')
    button_url = blocks.URLBlock(required=False,help_text='if added, used second')

    # def get_context(self, request,*args,**kwargs):
    #     context=super().get_context(self, request,*args,**kwargs)
    #     context['latest_posts']=BlogDetailPage.objects.live().public()[:3]
    #
    #     return context


    class Meta:
        template='streams/button_block.html'
        icon='placeholder'
        label='single button'
        value_class=LinkStructValue
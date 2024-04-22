from django.contrib.auth.models import User
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index

from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Homepage image"
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_subtext = models.CharField(
        blank=True,
        max_length=255, help_text="Write a sub explanation under the introduction"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on CTA button"
    )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA Link',
        help_text="Choose a page to link for the button"
    )
    primary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Primary Highlighted Page',
        help_text='Choose an article to be the primary highlighted page'
    )
    first_secondary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='First Secondary Highlighted Page',
        help_text='Choose an article to be the first secondary highlighted page'
    )
    second_secondary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Second Secondary Highlighted Page',
        help_text='Choose an article to be the second secondary highlighted page'
    )
    third_secondary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Third Secondary Highlighted Page',
        help_text='Choose an article to be the third secondary highlighted page'
    )

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        MultiFieldPanel(
            [
                FieldPanel('image'),
                FieldPanel('hero_text'),
                FieldPanel('hero_subtext'),
                FieldPanel('hero_cta'),
                FieldPanel('hero_cta_link')
            ],
            heading='Hero Section',
        ),
        FieldPanel('primary_highlight'),
        FieldPanel('first_secondary_highlight'),
        FieldPanel('second_secondary_highlight'),
        FieldPanel('third_secondary_highlight')
    ]


class ArticlePage(Page):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    header_title = models.CharField(
        blank=True,
        max_length=255
    )
    header_subtitle = models.CharField(
        blank=True,
        max_length=255
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Article image"
    )
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    primary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Primary Highlighted Page',
        help_text='Choose an article to be the primary highlighted page'
    )
    first_secondary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='First Secondary Highlighted Page',
        help_text='Choose an article to be the first secondary highlighted page'
    )
    second_secondary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Second Secondary Highlighted Page',
        help_text='Choose an article to be the second secondary highlighted page'
    )
    third_secondary_highlight = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Third Secondary Highlighted Page',
        help_text='Choose an article to be the third secondary highlighted page'
    )

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('header_title'),
        FieldPanel('header_subtitle'),
        FieldPanel('image'),
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('primary_highlight'),
        FieldPanel('first_secondary_highlight'),
        FieldPanel('second_secondary_highlight'),
        FieldPanel('third_secondary_highlight')
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date')
    ]


# Generated by Django 5.0.3 on 2024-04-14 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='first_secondary_highlight',
            field=models.ForeignKey(blank=True, help_text='Choose an article to be the first secondary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='First Secondary Highlighted Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta',
            field=models.CharField(blank=True, help_text='Text to display on CTA button', max_length=255, verbose_name='Hero CTA'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta_link',
            field=models.ForeignKey(blank=True, help_text='Choose a page to link for the button', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Hero CTA Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_subtext',
            field=models.CharField(blank=True, help_text='Write a sub explanation under the introduction', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_text',
            field=models.CharField(blank=True, help_text='Write an introduction for the site', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='primary_highlight',
            field=models.ForeignKey(blank=True, help_text='Choose an article to be the primary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Primary Highlighted Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_secondary_highlight',
            field=models.ForeignKey(blank=True, help_text='Choose an article to be the second secondary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Second Secondary Highlighted Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_secondary_highlight',
            field=models.ForeignKey(blank=True, help_text='Choose an article to be the third secondary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Third Secondary Highlighted Page'),
        ),
    ]

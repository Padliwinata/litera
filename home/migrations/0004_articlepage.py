# Generated by Django 5.0.3 on 2024-04-15 10:15

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_first_secondary_highlight_homepage_hero_cta_and_more'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('header_title', models.CharField(blank=True, max_length=255)),
                ('header_subtitle', models.CharField(blank=True, max_length=255)),
                ('date', models.DateField(verbose_name='Post date')),
                ('body', wagtail.fields.RichTextField(blank=True)),
                ('first_secondary_highlight', models.ForeignKey(blank=True, help_text='Choose an article to be the first secondary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='First Secondary Highlighted Page')),
                ('primary_highlight', models.ForeignKey(blank=True, help_text='Choose an article to be the primary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Primary Highlighted Page')),
                ('second_secondary_highlight', models.ForeignKey(blank=True, help_text='Choose an article to be the second secondary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Second Secondary Highlighted Page')),
                ('third_secondary_highlight', models.ForeignKey(blank=True, help_text='Choose an article to be the third secondary highlighted page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Third Secondary Highlighted Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

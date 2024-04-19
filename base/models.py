from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting
)


@register_setting
class NavigationSettings(BaseGenericSetting):
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)

    panels = [
        FieldPanel("instagram_url")
    ]


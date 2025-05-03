from django.db import models


class Dashboards(models.Model):
    """
    This model define dashboard
    """
    class Meta:
        db_table = 'dashboards'

    title = models.CharField(max_length=255)
    created_time = models.DateField(auto_now=True)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    
from django.db import models


class Parse_data(models.Model):
    name_app: str = models.CharField(verbose_name="name_app code", max_length=400, null=True, blank=True)
    name_company: str = models.CharField(verbose_name="name_company", max_length=400, null=True, blank=True)
    release_year: str = models.CharField(verbose_name="release_year", max_length=400, null=True, blank=True)
    email: str = models.CharField(verbose_name="email", max_length=400, null=True, blank=True)
    link: str = models.CharField(verbose_name="link", null=True, blank=True, max_length=700)

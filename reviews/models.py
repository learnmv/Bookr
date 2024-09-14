from django.db import models

class Publisher(models.Model):
    """A company that publishes books"""
    name = models.CharField(
        max_length=50,
        help_text="The name of the Publisher."
    )
    website = models.URLField(
        help_text="The Publishers Website."
    )
    email = models.EmailField(
        help_text="The Publisher's email address."
    )

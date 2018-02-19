from django.contrib.auth.models import User
from django.db import models

# App
from wac.apps.core.models import Location, Topic

class Profile(models.Model):
    """
    Extends from the user model
    """
    HE = 'he'
    SHE = 'she'
    THEY = 'they'
    PRONOUNS_CHOICE = (
        (HE, HE),
        (SHE, SHE),
        (THEY, THEY)
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    woman = models.NullBooleanField(
        null=True,
        blank=True
    )

    poc = models.NullBooleanField(
        null=True,
        blank=True
    )

    pronouns = models.CharField(
        max_length=10,
        choices=PRONOUNS_CHOICE,
        null=True,
        blank=True
    )

    position = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    organization = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    description = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    twitter = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    linkedin = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    website = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    page = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        default='registration'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def display_name(self):
        first_name = self.first_name
        last_name = self.last_name

        if first_name and last_name:
            return u"%s %s".strip() % (first_name, last_name)

        return None

    def __str__(self):
        return self.display_name()

    def __unicode__(self):
        return self.display_name()


class ProfileLocation(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class ProfileTopic(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    topic = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
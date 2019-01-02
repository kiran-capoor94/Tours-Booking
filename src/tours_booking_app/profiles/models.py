from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


User = settings.AUTH_USER_MODEL

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
)


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=_("profile"), on_delete=models.CASCADE)
    gender = models.CharField(max_length=150, choices=GENDER, default='male')
    about_me = models.TextField()
    website = models.URLField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(
        auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})

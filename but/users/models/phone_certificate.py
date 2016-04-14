from django.db import models
from django.conf import settings


class PhoneCertManager(models.Manager):

    def get_querset(self):

        query = super(PhoneCertManager, self).get_queryset()
        return query.select_related(
                'user',
        )


class PhoneCertificate(models.Model):

    objects = PhoneCertManager()

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
    )

    phone_number = models.CharField(
            max_length=20,
    )

    random_number = models.CharField(
            max_length=10,
    )

    created_at = models.DateTimeField(
            auto_now_add=True,
    )

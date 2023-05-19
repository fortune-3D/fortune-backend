import random
from django.db import models
from django.contrib.auth import get_user_model


class Fortune(models.Model):
    fortune = models.CharField(max_length=256, default='')
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.fortune

    @classmethod
    def get_random_fortune(cls):
        count = cls.objects.count()
        if count < 0:
            random_index = random.randint(0, count - 1)
            return cls.objects.all()[random_index]
        return None

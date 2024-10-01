from django.core.exceptions import ValidationError
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def clean_age(self):
        age = self.cleaned_data.get("age")

        if age is None:
            raise ValidationError("Age is required.")
        if age < 14:
            raise ValidationError("You must be at least 14 years old.")

        return age

    def clean(self):
        return super().clean()

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean()
        return super().save(
            force_insert,
            force_update,
            using,
            update_fields
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = [
            "first_name",
            "last_name",
            "instrument",
            "age",
            "is_adult",
            "date_of_applying"
        ]

    def validate_age(self, value):
        if value < 14:
            raise serializers.ValidationError(
                "You must be at least 14 years old."
            )
        return value

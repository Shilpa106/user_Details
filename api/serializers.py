from rest_framework import serializers
from . models import Person


class PersonSerializers(serializers.ModelSerializer):

    """
    Serializer for Person
    """

    class Meta:
        model = Person
        fields = ("id","firstName", "lastName", "email")
        

        
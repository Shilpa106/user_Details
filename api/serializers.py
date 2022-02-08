from rest_framework import serializers
from . models import Person


class PersonSerializers(serializers.ModelSerializer):

    '''
    :Serializer: Serializer fields for Person to serialize and deserialize json data
    '''

    class Meta:
        model = Person
        fields = ("id","first_name", "last_name", "email")
        

        
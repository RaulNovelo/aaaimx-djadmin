from rest_framework import serializers
from .models import Certificate

# Serializers define the API representation.
class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificate
        exclude = []
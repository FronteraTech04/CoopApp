from rest_framework import serializers
from app.core.common.serializers.serializer import PersonaSerializer
from app.core.socios.models import Socio

class SocioSerializer(serializers.ModelSerializer):

    persona = PersonaSerializer()

    class Meta:
        model = Socio
        fields = '__all__'
        

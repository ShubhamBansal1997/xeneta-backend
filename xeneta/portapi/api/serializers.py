""" Ports API Serializers """

# Third Party Stuff
from rest_framework import serializers

# xeneta Stuff
from xeneta.portapi.models import Ports


class AverageAPISerializer(serializers.Serializer):
    """
    AverageAPI Serializer
    """

    date_to = serializers.DateField(
        required=True, allow_null=False, format="YYYY-MM-DD"
    )
    date_from = serializers.DateField(
        required=True, allow_null=False, format="YYYY-MM-DD"
    )
    origin = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    destination = serializers.CharField(
        required=True, allow_null=False, allow_blank=False
    )


class PortsAPISerializer(serializers.ModelSerializer):
    """
    PortsAPISerializer
        Used to structure ports info
    """

    class Meta:
        model = Ports
        fields = "__all__"

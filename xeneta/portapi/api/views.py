# Third Party Stuff
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

# xeneta Stuff
from xeneta.base.api.mixins import MultipleSerializerMixin
from xeneta.portapi.models import Ports
from xeneta.portapi.services import average_prices_per_day

from .serializers import AverageAPISerializer, PortsAPISerializer


class PortsAPIViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):
    serializer_class = PortsAPISerializer
    queryset = Ports.objects.all()
    serializer_classes = {"rates": AverageAPISerializer}
    permission_classes = [AllowAny]

    @action(methods=["GET"], detail=False)
    def rates(self, request: Request) -> Response:
        """
        Ports Rates endpoints GET /ports?date_to=&date_from=&origin=&destination=
        """
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = average_prices_per_day(**serializer.validated_data)
        return Response(status=status.HTTP_200_OK, data=data)

    def list(self, request: Request) -> Response:
        """
        List endpoint GET /ports
        """
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def create(self, request) -> Response:
        """
        Create endpoint PORT /ports
        """
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request: Request, pk=None) -> Response:
        """
        Single Port endpoint GET /ports/<pk>
        """
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def update(self, request, pk=None) -> Response:
        """
        Update endpoint PUT /ports/<pk>
        """
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def partial_update(self, request: Request, pk=None) -> Response:
        """
        Partial Update endpoint PATCH /ports/<pk>
        """
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def destroy(self, request, pk=None) -> Response:
        """
        DELETE endpoint DELETE /ports/<pk>
        """
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

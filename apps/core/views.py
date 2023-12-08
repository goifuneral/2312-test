from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def pong(request):
    return Response("pong", status=status.HTTP_200_OK)

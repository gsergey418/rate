from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_rate(request):
    return Response()
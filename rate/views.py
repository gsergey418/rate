from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


@api_view(["GET"])
def get_rate(request):
    exchange_api_response = requests.get(
        "https://open.er-api.com/v6/latest/" + request.GET["from"])
    exchange_api_json = exchange_api_response.json()
    result = exchange_api_json["rates"][request.GET["to"]
                                        ] * int(request.GET["value"])
    return Response({
        "result": result
    })

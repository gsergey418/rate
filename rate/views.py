from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms import CharField, IntegerField
from django.core.exceptions import ValidationError

import requests
from requests.exceptions import RequestException


@api_view(["GET"])
def get_rate(request):

    try:
        from_cur = CharField(min_length=3, max_length=3).clean(
            request.GET["from"]).upper()
        to_cur = CharField(min_length=3, max_length=3).clean(
            request.GET["to"]).upper()
        amount = IntegerField().clean(request.GET["value"])
    except ValidationError:
        return Response({"message": "Необходимые параметры: from, to, value"}, status=400)

    try:
        exchange_api_response = requests.get(
            f"https://open.er-api.com/v6/latest/{from_cur}")
    except RequestException:
        return Response({"message": "Не получилось сделать запрос к стороннему сервису."}, status=504)

    exchange_api_json = exchange_api_response.json()
    result = exchange_api_json["rates"][to_cur] * amount

    return Response({
        "result": result
    })

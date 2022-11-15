import json
from http import HTTPStatus

from django.shortcuts import HttpResponse


def index(request):
    message = {"subdomain": str(request.subdomain) if request.subdomain else None}
    return HttpResponse(status=HTTPStatus.OK, content=json.dumps(message), content_type="application/json")

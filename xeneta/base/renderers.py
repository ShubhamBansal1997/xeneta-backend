# Third Party Stuff
from rest_framework.renderers import JSONRenderer


class XenetaApiRenderer(JSONRenderer):
    media_type = "application/vnd.xeneta+json"

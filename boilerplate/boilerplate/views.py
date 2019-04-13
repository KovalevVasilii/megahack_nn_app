import json

from django import views as vw

from boilerplate.models import Client, Dealer, Offer

from boilerplate.validations.offer_validation import validate_offer


class CheckOffer(vw.View):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        result = validate_offer(body['client'], body['dealer'], body['offer'])


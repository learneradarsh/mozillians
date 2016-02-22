from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from mozillians.users.views import (BaseProfileAdminAutocomplete, VouchedAutocomplete,
                                    VoucherAutocomplete)


urlpatterns = patterns(
    '',
    # Admin urls for django-autocomplete-light.
    url('vouchee-autocomplete/$', login_required(BaseProfileAdminAutocomplete.as_view()),
        name='vouchee-autocomplete'),
    url('voucher-autocomplete/$', login_required(VoucherAutocomplete.as_view()),
        name='voucher-autocomplete'),
    url('vouched-autocomplete/$', login_required(VouchedAutocomplete.as_view()),
        name='vouched-autocomplete'),
)

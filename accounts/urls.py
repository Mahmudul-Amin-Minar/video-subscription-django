from django.conf.urls import url

from .views import MembershipSelectView, payment, update_transaction

app_name = 'accounts'

urlpatterns = [
    url(r'^$', MembershipSelectView.as_view(), name='select'),
    url(r'^payment/', payment, name='payment'),
    url(r'^update-transaction/(?P<subscription_id>[\w-]+)$', update_transaction, name='update-transaction'),
]


from django.urls import path
from items.views import (
    create_checkout_session,
    CancelView,
    ItemPageView,
    SuccessView,
)

app_name = 'items'

urlpatterns = [
    path(
        'item/<int:pk>/',
        ItemPageView.as_view(),
        name='item_detail'
    ),
    path(
        'buy/<int:pk>/',
        create_checkout_session,
        name='create_checkout_session'
    ),
    path(
        'success/',
        SuccessView.as_view(),
        name='success'
    ),
    path(
        'cancel/',
        CancelView.as_view(),
        name='cancel'
    ),
]

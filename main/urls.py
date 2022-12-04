from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import main, apartments, main_sorted, sort_ap, ap_detail, add_review, default

urlpatterns = [
    path('', default, name='default'),
    path('main/', main, name='main'),
    path('ap/', apartments, name='ap'),
    path('sorted/', main_sorted, name='sorted'),
    path('ap_sorted/', sort_ap, name='ap_sorted'),
    path('save_review/', add_review, name='save_review'),
    path('apartment/<int:ap_id>/', ap_detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

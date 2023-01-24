from django.urls import path
from .views import LocalizacionView

urlpatterns=[
    path('localizaciones/',LocalizacionView.as_view(), name='loacalizaciones_list'),
    path('localizaciones/<int:id>',LocalizacionView.as_view(), name='loacalizaciones_process')
]
from django.urls import path

from .views import PatientCreateView


urlpatterns = [

    # صفحه ثبت بیمار
    path(
        "create/",
        PatientCreateView.as_view(),
        name="patient-create",
    ),

]
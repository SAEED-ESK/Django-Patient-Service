from django.urls import path

from .views import (
    PatientCreateView,
    PatientDeleteView,
    PatientListView,
    PatientDetailView,
    PatientUpdateView,
)


urlpatterns = [

    # لیست بیماران
    path(
        "",
        PatientListView.as_view(),
        name="patient-list",
    ),

    # ثبت بیمار جدید
    path(
        "create/",
        PatientCreateView.as_view(),
        name="patient-create",
    ),
    # جزئیات بیمار
    path(
        "<int:pk>/",
        PatientDetailView.as_view(),
        name="patient-detail",
    ),
    # ویرایش بیمار
    path(
        "<int:pk>/edit/",
        PatientUpdateView.as_view(),
        name="patient-edit",
    ),
    # حذف بیمار
    path(
        "<int:pk>/delete/",
        PatientDeleteView.as_view(),
        name="patient-delete",
    ),

]
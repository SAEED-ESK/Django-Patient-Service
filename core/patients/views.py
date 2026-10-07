from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView, DeleteView)

from .forms import PatientForm, PatientMedicationFormSet
from .models import Patient


class PatientCreateView(LoginRequiredMixin, CreateView):

    model = Patient
    form_class = PatientForm
    template_name = "patients/patient_form.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        if "medication_formset" not in context:

            context["medication_formset"] = PatientMedicationFormSet(
                instance=self.object
            )

        return context

    def form_valid(self, form):

        medication_formset = PatientMedicationFormSet(
            self.request.POST,
            instance=form.instance
        )

        if not medication_formset.is_valid():

            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    medication_formset=medication_formset,
                )
            )

        with transaction.atomic():

            form.instance.created_by = self.request.user

            self.object = form.save()

            medication_formset.instance = self.object
            medication_formset.save()

        messages.success(
            self.request,
            "بیمار با موفقیت ثبت شد."
        )

        return redirect(
            "/patients/"
        )


# =========================================================
# ویرایش بیمار
# =========================================================

class PatientUpdateView(LoginRequiredMixin, UpdateView):

    model = Patient
    form_class = PatientForm
    template_name = "patients/patient_edit.html"
    context_object_name = "patient"

    def get_queryset(self):
        return Patient.objects.filter(
            created_by=self.request.user
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        if "medication_formset" not in context:

            context["medication_formset"] = PatientMedicationFormSet(
                instance=self.object
            )

        return context

    def form_valid(self, form):

        medication_formset = PatientMedicationFormSet(
            self.request.POST,
            instance=self.object
        )

        if not medication_formset.is_valid():

            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    medication_formset=medication_formset,
                )
            )

        with transaction.atomic():

            self.object = form.save()

            medication_formset.instance = self.object
            medication_formset.save()

        messages.success(
            self.request,
            "اطلاعات بیمار با موفقیت بروزرسانی شد."
        )

        return redirect(
            "patient-detail",
            pk=self.object.pk
        )

# =========================================================
# لیست بیماران
# =========================================================

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "patients/patient_list.html"
    context_object_name = "patients"
    ordering = ["-created_at"]
    paginate_by = 10

    def get_queryset(self):
        queryset = Patient.objects.filter(
            created_by=self.request.user
        ).order_by("-created_at")

        # -----------------------------------------------------
        # جستجو بر اساس تشخیص روان پزشکی
        # -----------------------------------------------------

        search_query = self.request.GET.get("search", "").strip()

        if search_query:
            queryset = queryset.filter(
                psychiatric_diagnosis__icontains=search_query
            )

        # -----------------------------------------------------
        # فیلتر جنسیت
        # -----------------------------------------------------

        gender = self.request.GET.get("gender")

        if gender in ["male", "female"]:
            queryset = queryset.filter(
                gender=gender
            )

        # -----------------------------------------------------
        # فیلتر بیماری‌های همراه
        # -----------------------------------------------------

        if self.request.GET.get("diabetes") == "1":
            queryset = queryset.filter(
                diabetes=True
            )

        if self.request.GET.get("hypertension") == "1":
            queryset = queryset.filter(
                hypertension=True
            )

        if self.request.GET.get("obesity") == "1":
            queryset = queryset.filter(
                obesity=True
            )

        if self.request.GET.get("cardiovascular_disease") == "1":
            queryset = queryset.filter(
                cardiovascular_disease=True
            )

        return queryset

# =========================================================
# جزئیات یک بیمار
# =========================================================

class PatientDetailView(LoginRequiredMixin, DetailView):

    # مدل مورد استفاده
    model = Patient

    # Template صفحه جزئیات
    template_name = "patients/patient_detail.html"

    # نام آبجکت در Template
    context_object_name = "patient"

    def get_queryset(self):
        return Patient.objects.filter(
            created_by=self.request.user
        )

# =========================================================
# حذف بیمار
# =========================================================

class PatientDeleteView(LoginRequiredMixin, DeleteView):

    model = Patient
    template_name = "patients/patient_confirm_delete.html"
    context_object_name = "patient"

    def get_queryset(self):
        return Patient.objects.filter(
            created_by=self.request.user
        )

    def get_success_url(self):
        return "/patients/"

    def form_valid(self, form):

        messages.success(
            self.request,
            "پرونده بیمار با موفقیت حذف شد."
        )

        return super().form_valid(form)
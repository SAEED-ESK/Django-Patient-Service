from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView, DeleteView)

from .forms import PatientForm, PatientMedicationFormSet
from .models import Patient


class PatientCreateView(CreateView):

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

            self.object = form.save()

            medication_formset.instance = self.object
            medication_formset.save()

        messages.success(
            self.request,
            "بیمار با موفقیت ثبت شد."
        )

        return redirect(
            "/admin/patients/patient/"
        )

# =========================================================
# ویرایش بیمار
# =========================================================

class PatientUpdateView(UpdateView):

    model = Patient
    form_class = PatientForm
    template_name = "patients/patient_edit.html"
    context_object_name = "patient"

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

class PatientListView(ListView):

    # مدل مورد استفاده
    model = Patient

    # Template صفحه لیست
    template_name = "patients/patient_list.html"

    # نامی که لیست بیماران با آن به Template فرستاده می‌شود
    context_object_name = "patients"

    # جدیدترین بیماران اول نمایش داده شوند
    ordering = ["-created_at"]

# =========================================================
# جزئیات یک بیمار
# =========================================================

class PatientDetailView(DetailView):

    # مدل مورد استفاده
    model = Patient

    # Template صفحه جزئیات
    template_name = "patients/patient_detail.html"

    # نام آبجکت در Template
    context_object_name = "patient"

# =========================================================
# حذف بیمار
# =========================================================

class PatientDeleteView(DeleteView):

    model = Patient
    template_name = "patients/patient_confirm_delete.html"
    context_object_name = "patient"

    def get_success_url(self):
        return "/patients/"

    def form_valid(self, form):

        messages.success(
            self.request,
            "پرونده بیمار با موفقیت حذف شد."
        )

        return super().form_valid(form)
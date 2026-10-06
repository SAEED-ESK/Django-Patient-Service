from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic import CreateView

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
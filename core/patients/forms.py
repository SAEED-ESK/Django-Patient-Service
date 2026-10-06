from django import forms
from django.core.exceptions import ValidationError

from .models import Patient, PatientMedication


# =========================================================
# فرم اطلاعات بیمار
# مربوط به اطلاعات اصلی بیمار و بخش‌های پایش
# =========================================================

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

        # تمام فیلدهای مدل Patient را در فرم قرار می‌دهیم.
        fields = "__all__"

        # ظاهر ساده و قابل فهم فیلدها
        widgets = {

            # تاریخ شروع درمان
            "treatment_start_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            # تاریخ آخرین تغییر دارو یا دوز
            "last_medication_change": forms.DateInput(
                attrs={"type": "date"}
            ),

            # قسمت توضیحات
            "notes": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "توضیحات اضافی درباره بیمار..."
                }
            ),
        }

    # =====================================================
    # بررسی تاریخ‌ها
    #
    # آخرین تغییر دارو نمی‌تواند قبل از شروع درمان باشد.
    # =====================================================

    def clean(self):

        cleaned_data = super().clean()

        # تاریخ شروع درمان
        treatment_start = cleaned_data.get("treatment_start_date")

        # تاریخ آخرین تغییر
        last_change = cleaned_data.get("last_medication_change")

        # اگر هر دو تاریخ وارد شده باشند
        if treatment_start and last_change:

            if last_change < treatment_start:

                raise ValidationError(
                    "تاریخ آخرین تغییر دارو نمی‌تواند قبل از تاریخ شروع درمان باشد."
                )

        return cleaned_data


# =========================================================
# فرم داروی بیمار
# =========================================================

class PatientMedicationForm(forms.ModelForm):

    class Meta:
        model = PatientMedication

        fields = [
            "drug",
            "dose",
            "form",
        ]

    # بررسی دوز
    def clean_dose(self):

        dose = self.cleaned_data.get("dose")

        if dose is not None and dose <= 0:
            raise ValidationError(
                "دوز دارو باید بیشتر از صفر باشد."
            )

        return dose


# =========================================================
# بررسی مجموعه داروهای بیمار
#
# هر بیمار حداقل باید یک دارو داشته باشد.
# =========================================================

class PatientMedicationFormSetBase(forms.BaseInlineFormSet):

    def clean(self):

        super().clean()

        medication_count = 0

        for form in self.forms:

            if not hasattr(form, "cleaned_data"):
                continue

            if form.cleaned_data.get("DELETE"):
                continue

            if form.cleaned_data.get("drug"):
                medication_count += 1

        if medication_count == 0:
            raise ValidationError(
                "حداقل یک دارو باید برای بیمار ثبت شود."
            )


# =========================================================
# Formset نهایی داروها
# =========================================================

PatientMedicationFormSet = forms.inlineformset_factory(
    Patient,
    PatientMedication,
    form=PatientMedicationForm,
    formset=PatientMedicationFormSetBase,
    extra=1,
    can_delete=True,
)
import jdatetime
from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from .models import Patient, PatientMedication


# =========================================================
# فیلد تاریخ شمسی
# =========================================================

class JalaliDateField(forms.DateField):
    """
    تاریخ شمسی را از کاربر دریافت می‌کند
    و قبل از ذخیره به تاریخ میلادی تبدیل می‌کند.
    """

    def to_python(self, value):
        if not value:
            return None

        if isinstance(value, date):
            return value

        value = value.strip().replace("-", "/")

        try:
            year, month, day = map(int, value.split("/"))

            jalali_date = jdatetime.date(year, month, day)

            return jalali_date.togregorian()

        except (ValueError, TypeError):
            raise forms.ValidationError(
                "تاریخ را به صورت صحیح وارد کنید. مثال: 1405/07/15"
            )

    def prepare_value(self, value):
        """
        هنگام نمایش تاریخ ذخیره‌شده،
        تاریخ میلادی را به شمسی تبدیل می‌کند.
        """

        if not value:
            return ""

        if isinstance(value, date):
            jalali_date = jdatetime.date.fromgregorian(date=value)

            return jalali_date.strftime("%Y/%m/%d")

        return value


# =========================================================
# فرم بیمار
# =========================================================

class PatientForm(forms.ModelForm):

    treatment_start_date = JalaliDateField(
        label="تاریخ شروع درمان"
    )

    last_medication_change = JalaliDateField(
        label="آخرین تغییر دارو یا دوز"
    )

    class Meta:
        model = Patient
        fields = "__all__"

        widgets = {
            "treatment_start_date": forms.TextInput(
                attrs={
                    "placeholder": "1405/07/15",
                    "autocomplete": "off",
                    "class": "jalali-date-input",
                }
            ),
            "last_medication_change": forms.TextInput(
                attrs={
                    "placeholder": "1405/07/15",
                    "autocomplete": "off",
                    "class": "jalali-date-input",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        treatment_start_date = cleaned_data.get(
            "treatment_start_date"
        )

        last_medication_change = cleaned_data.get(
            "last_medication_change"
        )

        if (
            treatment_start_date
            and last_medication_change
            and last_medication_change < treatment_start_date
        ):
            raise forms.ValidationError(
                "تاریخ آخرین تغییر دارو نمی‌تواند قبل از تاریخ شروع درمان باشد."
            )

        return cleaned_data


# =========================================================
# فرم دارو
# =========================================================

class PatientMedicationForm(forms.ModelForm):

    class Meta:
        model = PatientMedication

        fields = [
            "drug",
            "dose",
            "form",
        ]

    def clean_dose(self):
        dose = self.cleaned_data.get("dose")

        if dose is not None and dose <= 0:
            raise ValidationError(
                "دوز دارو باید بیشتر از صفر باشد."
            )

        return dose


# =========================================================
# Formset داروها
# =========================================================

class PatientMedicationFormSetBase(forms.BaseInlineFormSet):

    def clean(self):
        super().clean()

        medication_count = 0

        for form in self.forms:

            if not hasattr(form, "cleaned_data"):
                continue

            # دارویی که حذف شده نباید در شمارش حساب شود
            if form.cleaned_data.get("DELETE"):
                continue

            # فرم کاملاً خالی را نادیده می‌گیریم
            if not form.cleaned_data.get("drug"):
                continue

            medication_count += 1

        if medication_count == 0:
            raise ValidationError(
                "حداقل یک دارو باید برای بیمار ثبت شود."
            )


# =========================================================
# Formset نهایی
# =========================================================

PatientMedicationFormSet = forms.inlineformset_factory(
    Patient,
    PatientMedication,
    form=PatientMedicationForm,
    formset=PatientMedicationFormSetBase,
    extra=1,
    can_delete=True,
)
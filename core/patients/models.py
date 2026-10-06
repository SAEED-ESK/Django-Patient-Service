from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# =========================================================
# مدل اصلی بیمار
# مربوط به بخش‌های 1 تا 17 فرم بیمار
# =========================================================

class Patient(models.Model):

    # -----------------------------------------------------
    # 1. سن
    # عدد بین 18 تا 100
    # -----------------------------------------------------
    age = models.PositiveIntegerField(
        verbose_name="سن",
        validators=[
            MinValueValidator(18),
            MaxValueValidator(100),
        ]
    )

    # -----------------------------------------------------
    # 2. جنس
    # انتخاب بین مرد و زن
    # -----------------------------------------------------
    gender = models.CharField(
        max_length=10,
        choices=[
            ("male", "مرد"),
            ("female", "زن"),
        ],
        verbose_name="جنس"
    )

    # -----------------------------------------------------
    # 3. تشخیص روان پزشکی
    # یک متن کوتاه که خودمان وارد می‌کنیم
    # مثال: اسکیزوفرنی
    # -----------------------------------------------------
    psychiatric_diagnosis = models.CharField(
        max_length=255,
        verbose_name="تشخیص روان پزشکی"
    )

    # =====================================================
    # 4. بیماری‌های متابولیک / قلبی همراه
    # هر کدام فقط دارد / ندارد
    # =====================================================

    # دیابت
    diabetes = models.BooleanField(
        default=False,
        verbose_name="دیابت"
    )

    # پرفشاری خون
    hypertension = models.BooleanField(
        default=False,
        verbose_name="پرفشاری خون"
    )

    # دیس‌لیپیدمی
    dyslipidemia = models.BooleanField(
        default=False,
        verbose_name="دیس‌لیپیدمی"
    )

    # چاقی
    obesity = models.BooleanField(
        default=False,
        verbose_name="چاقی"
    )

    # بیماری قلبی عروقی
    cardiovascular_disease = models.BooleanField(
        default=False,
        verbose_name="بیماری قلبی عروقی"
    )

    # =====================================================
    # 8. مدت درمان از شروع
    # تاریخ اولین مراجعه / شروع درمان
    #
    # خود "مدت درمان" را ذخیره نمی‌کنیم.
    # فقط تاریخ شروع را ذخیره می‌کنیم و بعداً مدت را حساب می‌کنیم.
    # =====================================================

    treatment_start_date = models.DateField(
        verbose_name="تاریخ شروع درمان"
    )

    # =====================================================
    # 9. آخرین تغییر
    # آخرین تاریخی که پزشک دارو یا دوز آن را تغییر داده
    # =====================================================

    last_medication_change = models.DateField(
        verbose_name="آخرین تغییر دارو یا دوز"
    )

    # =====================================================
    # 10. پایش وزن / BMI
    # =====================================================

    weight_before_treatment = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - قبل از شروع درمان"
    )

    weight_week_1 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - هفته اول"
    )

    weight_week_2 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - هفته دوم"
    )

    weight_week_3 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - هفته سوم"
    )

    weight_week_4 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - هفته چهارم"
    )

    weight_week_5 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - هفته پنجم"
    )

    weight_week_6 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - هفته ششم"
    )

    weight_week_12 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - هفته دوازدهم"
    )

    weight_year_1 = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - یک سال"
    )

    weight_annually = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - سالانه"
    )

    weight_not_indicated = models.BooleanField(
        default=False,
        verbose_name="وزن/BMI - فاقد اندیکاسیون"
    )

    # =====================================================
    # 11. پایش دور کمر
    # =====================================================

    waist_before_treatment = models.BooleanField(
        default=False,
        verbose_name="دور کمر - قبل از شروع درمان"
    )

    waist_year_1 = models.BooleanField(
        default=False,
        verbose_name="دور کمر - یک سال"
    )

    waist_annually = models.BooleanField(
        default=False,
        verbose_name="دور کمر - سالانه"
    )

    waist_not_indicated = models.BooleanField(
        default=False,
        verbose_name="دور کمر - فاقد اندیکاسیون"
    )

    # =====================================================
    # 12. پایش فشار خون / نبض
    # =====================================================

    blood_pressure_before_treatment = models.BooleanField(
        default=False,
        verbose_name="فشار خون/نبض - قبل از شروع درمان"
    )

    blood_pressure_week_12 = models.BooleanField(
        default=False,
        verbose_name="فشار خون/نبض - هفته دوازدهم"
    )

    blood_pressure_year_1 = models.BooleanField(
        default=False,
        verbose_name="فشار خون/نبض - یک سال"
    )

    blood_pressure_annually = models.BooleanField(
        default=False,
        verbose_name="فشار خون/نبض - سالانه"
    )

    blood_pressure_not_indicated = models.BooleanField(
        default=False,
        verbose_name="فشار خون/نبض - فاقد اندیکاسیون"
    )

    # =====================================================
    # 13. پایش گلوکز ناشتا / HbA1c
    # =====================================================

    glucose_before_treatment = models.BooleanField(
        default=False,
        verbose_name="گلوکز/HbA1c - قبل از شروع درمان"
    )

    glucose_week_12 = models.BooleanField(
        default=False,
        verbose_name="گلوکز/HbA1c - هفته دوازدهم"
    )

    glucose_year_1 = models.BooleanField(
        default=False,
        verbose_name="گلوکز/HbA1c - یک سال"
    )

    glucose_annually = models.BooleanField(
        default=False,
        verbose_name="گلوکز/HbA1c - سالانه"
    )

    glucose_not_indicated = models.BooleanField(
        default=False,
        verbose_name="گلوکز/HbA1c - فاقد اندیکاسیون"
    )

    # =====================================================
    # 14. پایش پروفایل چربی
    # =====================================================

    lipid_before_treatment = models.BooleanField(
        default=False,
        verbose_name="پروفایل چربی - قبل از شروع درمان"
    )

    lipid_week_12 = models.BooleanField(
        default=False,
        verbose_name="پروفایل چربی - هفته دوازدهم"
    )

    lipid_year_1 = models.BooleanField(
        default=False,
        verbose_name="پروفایل چربی - یک سال"
    )

    lipid_annually = models.BooleanField(
        default=False,
        verbose_name="پروفایل چربی - سالانه"
    )

    lipid_not_indicated = models.BooleanField(
        default=False,
        verbose_name="پروفایل چربی - فاقد اندیکاسیون"
    )

    # =====================================================
    # 15. پایش پرولاکتین
    # =====================================================

    prolactin_before_treatment = models.BooleanField(
        default=False,
        verbose_name="پرولاکتین - قبل از شروع درمان"
    )

    # آیا نیاز بالینی وجود دارد؟
    prolactin_clinical_need = models.BooleanField(
        default=False,
        verbose_name="پرولاکتین - نیاز بالینی"
    )

    # در صورت نیاز بالینی، هفته دوازدهم
    prolactin_week_12 = models.BooleanField(
        default=False,
        verbose_name="پرولاکتین - نیاز بالینی - هفته دوازدهم"
    )

    # در صورت نیاز بالینی، یک سال
    prolactin_year_1 = models.BooleanField(
        default=False,
        verbose_name="پرولاکتین - نیاز بالینی - یک سال"
    )

    # در صورت وجود علائم
    prolactin_symptoms = models.BooleanField(
        default=False,
        verbose_name="پرولاکتین - درصورت علائم"
    )

    # فاقد اندیکاسیون
    prolactin_not_indicated = models.BooleanField(
        default=False,
        verbose_name="پرولاکتین - فاقد اندیکاسیون"
    )

    # =====================================================
    # 16. ارزیابی اختلالات حرکتی
    # =====================================================

    movement_before_treatment = models.BooleanField(
        default=False,
        verbose_name="اختلالات حرکتی - قبل از شروع درمان"
    )

    movement_weekly = models.BooleanField(
        default=False,
        verbose_name="اختلالات حرکتی - هفتگی"
    )

    movement_week_12 = models.BooleanField(
        default=False,
        verbose_name="اختلالات حرکتی - هفته دوازدهم"
    )

    movement_year_1 = models.BooleanField(
        default=False,
        verbose_name="اختلالات حرکتی - یک سال"
    )

    movement_periodically = models.BooleanField(
        default=False,
        verbose_name="اختلالات حرکتی - دوره‌ای"
    )

    movement_not_indicated = models.BooleanField(
        default=False,
        verbose_name="اختلالات حرکتی - فاقد اندیکاسیون"
    )

    # =====================================================
    # 17. ECG
    # =====================================================

    ecg_before_treatment = models.BooleanField(
        default=False,
        verbose_name="ECG - قبل از شروع درمان"
    )

    ecg_not_indicated = models.BooleanField(
        default=False,
        verbose_name="ECG - فاقد اندیکاسیون"
    )

    # =====================================================
    # توضیحات
    # برای نوشتن هر نکته یا توضیح اضافی درباره بیمار
    # این قسمت اختیاری است.
    # =====================================================

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    # =====================================================
    # تاریخ ثبت بیمار
    # این دو مورد را خود Django پر می‌کند.
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    # =====================================================
    # بررسی پلی‌فارماسی
    # اگر بیمار بیشتر از یک دارو داشته باشد،
    # یعنی بیمار در وضعیت پلی‌فارماسی است.
    # =====================================================

    @property
    def is_polypharmacy(self):
        return self.medications.count() > 1


    # =====================================================
    # 10. وضعیت پایش وزن / BMI
    #
    # اگر همه موارد لازم تیک خورده باشند:
    #     منطبق
    #
    # اگر فقط فاقد اندیکاسیون تیک خورده باشد:
    #     فاقد اندیکاسیون
    #
    # در هر حالت دیگری:
    #     نامنطبق
    # =====================================================

    def get_weight_status(self):

        # اگر فاقد اندیکاسیون انتخاب شده باشد،
        # نباید هیچ گزینه دیگری انتخاب شده باشد.
        if self.weight_not_indicated:
            other_checks = [
                self.weight_before_treatment,
                self.weight_week_1,
                self.weight_week_2,
                self.weight_week_3,
                self.weight_week_4,
                self.weight_week_5,
                self.weight_week_6,
                self.weight_week_12,
                self.weight_year_1,
                self.weight_annually,
            ]

            if any(other_checks):
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        # تمام بررسی‌های لازم باید انجام شده باشند.
        required_checks = [
            self.weight_before_treatment,
            self.weight_week_1,
            self.weight_week_2,
            self.weight_week_3,
            self.weight_week_4,
            self.weight_week_5,
            self.weight_week_6,
            self.weight_week_12,
            self.weight_year_1,
            self.weight_annually,
        ]

        if all(required_checks):
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # 11. وضعیت پایش دور کمر
    # =====================================================

    def get_waist_status(self):

        if self.waist_not_indicated:

            other_checks = [
                self.waist_before_treatment,
                self.waist_year_1,
                self.waist_annually,
            ]

            if any(other_checks):
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        required_checks = [
            self.waist_before_treatment,
            self.waist_year_1,
            self.waist_annually,
        ]

        if all(required_checks):
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # 12. وضعیت پایش فشار خون / نبض
    # =====================================================

    def get_blood_pressure_status(self):

        if self.blood_pressure_not_indicated:

            other_checks = [
                self.blood_pressure_before_treatment,
                self.blood_pressure_week_12,
                self.blood_pressure_year_1,
                self.blood_pressure_annually,
            ]

            if any(other_checks):
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        required_checks = [
            self.blood_pressure_before_treatment,
            self.blood_pressure_week_12,
            self.blood_pressure_year_1,
            self.blood_pressure_annually,
        ]

        if all(required_checks):
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # 13. وضعیت پایش گلوکز ناشتا / HbA1c
    # =====================================================

    def get_glucose_status(self):

        if self.glucose_not_indicated:

            other_checks = [
                self.glucose_before_treatment,
                self.glucose_week_12,
                self.glucose_year_1,
                self.glucose_annually,
            ]

            if any(other_checks):
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        required_checks = [
            self.glucose_before_treatment,
            self.glucose_week_12,
            self.glucose_year_1,
            self.glucose_annually,
        ]

        if all(required_checks):
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # 14. وضعیت پایش پروفایل چربی
    # =====================================================

    def get_lipid_status(self):

        if self.lipid_not_indicated:

            other_checks = [
                self.lipid_before_treatment,
                self.lipid_week_12,
                self.lipid_year_1,
                self.lipid_annually,
            ]

            if any(other_checks):
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        required_checks = [
            self.lipid_before_treatment,
            self.lipid_week_12,
            self.lipid_year_1,
            self.lipid_annually,
        ]

        if all(required_checks):
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # 15. وضعیت پایش پرولاکتین
    # =====================================================

    def get_prolactin_status(self):

        # اگر فقط فاقد اندیکاسیون انتخاب شده باشد
        if self.prolactin_not_indicated:

            other_checks = [
                self.prolactin_before_treatment,
                self.prolactin_clinical_need,
                self.prolactin_week_12,
                self.prolactin_year_1,
                self.prolactin_symptoms,
            ]

            if any(other_checks):
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        # قبل از شروع درمان باید حتماً بررسی شده باشد.
        if not self.prolactin_before_treatment:
            return "نامنطبق"

        # اگر نیاز بالینی انتخاب نشده باشد،
        # فقط بررسی قبل از درمان کافی است.
        if not self.prolactin_clinical_need:
            return "منطبق"

        # اگر نیاز بالینی انتخاب شده باشد،
        # هفته 12 و یک سال باید هر دو بررسی شده باشند.
        if (
            self.prolactin_week_12
            and self.prolactin_year_1
        ):
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # 16. وضعیت ارزیابی اختلالات حرکتی
    # =====================================================

    def get_movement_status(self):

        if self.movement_not_indicated:

            other_checks = [
                self.movement_before_treatment,
                self.movement_weekly,
                self.movement_week_12,
                self.movement_year_1,
                self.movement_periodically,
            ]

            if any(other_checks):
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        required_checks = [
            self.movement_before_treatment,
            self.movement_weekly,
            self.movement_week_12,
            self.movement_year_1,
            self.movement_periodically,
        ]

        if all(required_checks):
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # 17. وضعیت ECG
    # =====================================================

    def get_ecg_status(self):

        if self.ecg_not_indicated:

            if self.ecg_before_treatment:
                return "نامنطبق"

            return "فاقد اندیکاسیون"

        # اگر فاقد اندیکاسیون انتخاب نشده،
        # بررسی قبل از درمان باید انجام شده باشد.
        if self.ecg_before_treatment:
            return "منطبق"

        return "نامنطبق"


    # =====================================================
    # وضعیت کلی انطباق بیمار
    #
    # اگر هر 8 مورد:
    # منطبق یا فاقد اندیکاسیون باشند
    #     انطباق کامل
    #
    # اگر بعضی نامنطبق باشند:
    #     انطباق نسبی
    #
    # اگر هر 8 مورد نامنطبق باشند:
    #     عدم انطباق
    # =====================================================

    def get_overall_compliance(self):

        statuses = [
            self.get_weight_status(),
            self.get_waist_status(),
            self.get_blood_pressure_status(),
            self.get_glucose_status(),
            self.get_lipid_status(),
            self.get_prolactin_status(),
            self.get_movement_status(),
            self.get_ecg_status(),
        ]

        # اگر همه موارد نامنطبق باشند
        if all(status == "نامنطبق" for status in statuses):
            return "عدم انطباق"

        # اگر هیچ مورد نامنطبقی وجود نداشته باشد
        if all(status != "نامنطبق" for status in statuses):
            return "انطباق کامل"

        # یعنی بعضی منطبق/فاقد اندیکاسیون
        # و بعضی نامنطبق هستند.
        return "انطباق نسبی"


    # =====================================================
    # بررسی تاریخ‌ها
    #
    # آخرین تغییر دارو یا دوز نباید قبل از شروع درمان باشد.
    # =====================================================

    def clean(self):

        from django.core.exceptions import ValidationError

        if self.last_medication_change < self.treatment_start_date:
            raise ValidationError(
                "تاریخ آخرین تغییر دارو نمی‌تواند قبل از تاریخ شروع درمان باشد."
            )


    # =====================================================
    # نمایش بیمار
    # =====================================================

    def __str__(self):
        return f"بیمار شماره {self.id}"


# =========================================================
# داروهای بیمار
#
# هر بیمار می‌تواند یک یا چند دارو داشته باشد.
# به همین دلیل این قسمت را از Patient جدا می‌کنیم.
# =========================================================

class PatientMedication(models.Model):

    # بیمار مربوط به این دارو
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="medications",
        verbose_name="بیمار"
    )

    # -----------------------------------------------------
    # 5. نام آنتی‌سایکوتیک نسل دوم
    # -----------------------------------------------------

    drug = models.CharField(
        max_length=30,
        choices=[
            ("olanzapine", "الانزاپین"),
            ("clozapine", "کلوزاپین"),
            ("risperidone", "ریسپریدون"),
            ("aripiprazole", "آریپیپرازول"),
            ("quetiapine", "کوئتیاپین"),
            ("ziprasidone", "زیپراسیدون"),
            ("paliperidone", "پالیپریدون"),
            ("asenapine", "آسناپین"),
            ("iloperidone", "ایلوپریدون"),
            ("lurasidone", "لوراسیدون"),
        ],
        verbose_name="نام آنتی‌سایکوتیک نسل دوم"
    )

    # -----------------------------------------------------
    # 6. دوز روزانه
    # عدد صحیح مثبت
    # مثال: 5 ، 10 ، 20
    # -----------------------------------------------------

    dose = models.PositiveIntegerField(
        verbose_name="دوز روزانه"
    )

    # -----------------------------------------------------
    # 7. فرم دارویی
    # خوراکی / طولانی‌اثر تزریقی
    # -----------------------------------------------------

    form = models.CharField(
        max_length=20,
        choices=[
            ("oral", "خوراکی"),
            ("injection", "طولانی‌اثر تزریقی"),
        ],
        verbose_name="فرم دارویی"
    )

    def __str__(self):
        return f"{self.get_drug_display()} - {self.dose}"
    
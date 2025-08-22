import pandas as pd
import re

def check_fake_record(name, age, phone, national_id=None):
    reasons = []

    phone_str = str(phone)
    if phone_str.startswith("9") and len(phone_str) == 10:
        phone_str = "0" + phone_str

    # سن
    try:
        age = int(age)
        if not (0 < age < 120):
            reasons.append("Invalid Age")
    except:
        reasons.append("Invalid Age")

    # شماره تلفن
    if not re.fullmatch(r"09\d{9}", phone_str):
        reasons.append("Invalid Phone")

    # اسم
    if not re.fullmatch(r"[آ-ی]+ [آ-ی]+", str(name)):
        reasons.append("Invalid Name")

    # کد ملی
    if national_id is not None:
        if not re.fullmatch(r"\d{10}", str(national_id)):
            reasons.append("Invalid NationalID")

    is_fake = len(reasons) > 0
    return pd.Series([is_fake, ", ".join(reasons)])
import re

def normalize_marker(name: str) -> str:
    name = name.lower().strip()

    # Remove text inside brackets
    name = re.sub(r"\(.*?\)", "", name)

    # Replace hyphens with spaces
    name = name.replace("-", " ")

    # Remove extra spaces
    name = re.sub(r"\s+", " ", name).strip()

    # ----------------------------
    # Smart normalization
    # ----------------------------

    # TSH
    if "tsh" in name:
        return "tsh"

    # Vitamin D
    if "vitamin d" in name:
        return "vitamin_d"

    # Vitamin B12
    if "vitamin b12" in name or "vitamin b 12" in name:
        return "vitamin_b12"

    # HbA1c
    if "glycosylated" in name or "hba1c" in name:
        return "hba1c"

    # MCH
    if "mean corpuscular hemoglobin" in name or name == "mch":
        return "mch"

    # MCHC
    if "mchc" in name or "mean corp.hemo. conc" in name:
        return "mchc"

    # RDWI
    if "rdwi" in name or "red cell distribution width index" in name:
        return "rdwi"

    # Mentzer Index
    if "mentzer" in name:
        return "mentzer"

    # LDL
    if "ldl" in name:
        return "ldl"

    # HDL
    if "hdl" in name:
        return "hdl"

    # Cholesterol
    if "cholesterol" in name:
        return "cholesterol"

    # Hemoglobin
    if (
        "hemoglobin" in name
        or "haemoglobin" in name
        or name == "hb"
    ):
        return "hemoglobin"

    # Blood Urea / BUN
    if "blood urea nitrogen" in name:
        return "bun"

    if name == "blood urea":
        return "blood_urea"

    # Default
    return name
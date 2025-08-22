def calculate_insurance_price(disease):
    price_table = {
        "سرطان": 1000000,
        "دیابت": 500000,
        "فشارخون": 300000,
        "سایر": 200000
    }
    return price_table.get(disease, 200000)
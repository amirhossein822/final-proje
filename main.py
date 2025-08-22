import pandas as pd
from modules.rule_based import check_fake_record
from modules.feature_engineering import create_features
from modules.ml_model import train_ml_model
from modules.insurance_pricing import calculate_insurance_price
from modules.reporting import generate_report

def main(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # 1. اعتبارسنجی رکوردها
    df[['IsFake_RuleBased', 'FakeReason']] = df.apply(
        lambda row: check_fake_record(
            row['Name'], row['Age'], row['Phone'], row.get('NationalID', None)
        ), axis=1
    )

    # 2. ویژگی‌سازی
    df = create_features(df)

    # 3. آموزش مدل و پیش‌بینی ML
    clf, scaler, features = train_ml_model(df)
    if clf is not None:
        X_scaled = scaler.transform(df[features])
        df['ML_Prob'] = clf.predict_proba(X_scaled)[:,1]
    else:
        df['ML_Prob'] = df['IsFake_RuleBased'].apply(lambda x: 1.0 if x else 0.0)

    # 4. تصمیم نهایی
    df['IsFake_Final'] = df.apply(lambda row: True if row['IsFake_RuleBased'] else (row['ML_Prob']>0.5), axis=1)

    # 5. محاسبه قیمت بیمه
    df['InsurancePrice'] = df['Disease'].apply(calculate_insurance_price)

    # ذخیره CSV خروجی
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')

    # تولید گزارش
    generate_report(df, "report.png")
    print(f"✅ پروژه کامل اجرا شد. خروجی: {output_csv}, گزارش: report.png")

if __name__ == "__main__":
    main("insurance_data.csv", "insurance_checked_ml.csv")

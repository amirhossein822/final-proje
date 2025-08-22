import matplotlib.pyplot as plt

def generate_report(df, output_file):
    fig, axes = plt.subplots(1, 3, figsize=(18,5))

    # Pie chart: Fake vs Real
    df['IsFake_Final'].value_counts().plot.pie(ax=axes[0], autopct='%1.1f%%', labels=['Real','Fake'])
    axes[0].set_title("وضعیت رکوردها")

    # Bar chart: Fake reasons
    reasons = df['FakeReason'].value_counts()
    reasons.plot.bar(ax=axes[1])
    axes[1].set_title("دلایل جعلی بودن")

    # Bar chart: Average insurance price per disease
    df.groupby('Disease')['InsurancePrice'].mean().plot.bar(ax=axes[2])
    axes[2].set_title("میانگین قیمت بیمه بر اساس بیماری")

    plt.tight_layout()
    plt.savefig(output_file)
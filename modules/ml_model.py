from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def train_ml_model(df):
    features = ['name_length', 'has_space_in_name', 'phone_length', 'phone_starts09',
                'nationalid_length', 'all_digits_nationalid', 'non_farsi_chars_in_name', 'Age']
    X = df[features]
    y = df['IsFake_RuleBased']

    if len(y.unique()) < 2:
        return None, None, features

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    return clf, scaler, features
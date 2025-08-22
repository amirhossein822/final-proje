import pandas as pd
import re

def create_features(df):
    df['name_length'] = df['Name'].apply(lambda x: len(str(x)))
    df['has_space_in_name'] = df['Name'].apply(lambda x: 1 if ' ' in str(x) else 0)
    df['phone_length'] = df['Phone'].apply(lambda x: len(str(x)))
    df['phone_starts09'] = df['Phone'].apply(lambda x: 1 if str(x).startswith('09') else 0)
    df['nationalid_length'] = df['NationalID'].apply(lambda x: len(str(x)))
    df['all_digits_nationalid'] = df['NationalID'].apply(lambda x: 1 if str(x).isdigit() else 0)
    df['non_farsi_chars_in_name'] = df['Name'].apply(lambda x: len([c for c in str(x) if not re.match(r"[آ-ی\s]", c)]))
    df['Age'] = df['Age'].apply(lambda x: int(x) if str(x).isdigit() else 0)
    return df
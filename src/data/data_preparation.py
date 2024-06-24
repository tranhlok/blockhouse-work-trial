# src/data/data_preparation.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import torch

class DataPreparation:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tech_indicators_data = pd.read_csv(file_path)
        self.label_encoders = {}
        self.scaler = StandardScaler()

    def label_encode(self):
        categorical_cols = self.tech_indicators_data.select_dtypes(include=['object', 'category']).columns
        for col in categorical_cols:
            le = LabelEncoder()
            self.tech_indicators_data[col] = le.fit_transform(self.tech_indicators_data[col].astype(str))
            self.label_encoders[col] = le

    def separate_features_labels(self):
        features = self.tech_indicators_data.drop(['side'], axis=1)
        labels = self.tech_indicators_data['side']
        return features, labels

    def standardize_features(self, features):
        return self.scaler.fit_transform(features)

    def prepare_data(self):
        self.label_encode()
        features, labels = self.separate_features_labels()
        features_scaled = self.standardize_features(features)
        X_train, X_val, y_train, y_val = train_test_split(features_scaled, labels, test_size=0.2, random_state=42)
        X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
        y_train_tensor = torch.tensor(y_train.values, dtype=torch.long)
        X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
        y_val_tensor = torch.tensor(y_val.values, dtype=torch.long)
        return X_train_tensor, y_train_tensor, X_val_tensor, y_val_tensor

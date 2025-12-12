import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    X = data.drop("threat", axis=1)
    y = data["threat"]
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def predict_threat(model, sample):
    prediction = model.predict([sample])
    return "Threat Detected" if prediction[0] == 1 else "No Threat"

if __name__ == "__main__":
    data = load_data("network_traffic.csv")
    model = train_model(data)
    
    test_sample = [120, 80, 1]
    print(predict_threat(model, test_sample))

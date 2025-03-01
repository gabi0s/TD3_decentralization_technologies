import requests
import numpy as np

# API endpoints for the models
model_urls = [
    "https://e78e-89-30-29-68.ngrok-free.app/predict", #gab
    "https://a1d9-89-30-29-68.ngrok-free.app/predict"  #théo
    "https://486f-2a01-cb00-adb-fe00-79df-dfdd-d24c-d026.ngrok-free.app/predict" #victor
]

# Initial weights and deposits
weights = np.array([0.5, 0.5])
deposits = np.array([1000, 1000])

# Slashing factor
slashing_factor = 0.1

# Ground truth label (example)
ground_truth = 0

# Request body with flower features
request_body = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

def fetch_predictions(urls, body):
    predictions = []
    for url in urls:
        response = requests.post(url, json=body)
        data = response.json()
        predictions.append(data['probability'][0])
    return predictions

def aggregate_predictions(predictions, weights):
    weighted_probabilities = np.average(predictions, axis=0, weights=weights)
    consensus_prediction = np.argmax(weighted_probabilities)
    return consensus_prediction, weighted_probabilities

def evaluate_performance(consensus_prediction, ground_truth):
    return consensus_prediction == ground_truth

def adjust_weights_and_deposits(predictions, ground_truth, weights, deposits, slashing_factor):
    performances = [np.argmax(pred) == ground_truth for pred in predictions]
    total_performance = sum(performances)
    new_weights = np.array([performance / total_performance for performance in performances])
    new_deposits = deposits - (1 - np.array(performances)) * slashing_factor * deposits
    return new_weights, new_deposits

# Fetch predictions from models
predictions = fetch_predictions(model_urls, request_body)

# Aggregate predictions
consensus_prediction, aggregated_probabilities = aggregate_predictions(predictions, weights)

# Evaluate performance
accuracy = evaluate_performance(consensus_prediction, ground_truth)

# Adjust weights and deposits
weights, deposits = adjust_weights_and_deposits(predictions, ground_truth, weights, deposits, slashing_factor)

print("Aggregated Probabilities:", aggregated_probabilities)
print("Consensus Prediction:", consensus_prediction)
print("Accuracy:", accuracy)
print("Adjusted Weights:", weights)
print("Updated Deposits:", deposits)

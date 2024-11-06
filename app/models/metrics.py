def compute_metrics(TP, TN, FP, FN):
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (TP + TN) / (TP + TN + FP + FN) if (TP + TN + FP + FN) > 0 else 0
    total = TP + TN + FP + FN
    return precision, recall, f1_score, accuracy, total

def interpret_accuracy(accuracy):
    if 0.00 <= accuracy <= 0.10:
        return "No Agreement"
    elif 0.11 <= accuracy <= 0.40:
        return "Slight Agreement"
    elif 0.41 <= accuracy <= 0.60:
        return "Moderate Agreement"
    elif 0.61 <= accuracy <= 0.80:
        return "Substantial Agreement"
    elif 0.81 <= accuracy <= 0.99:
        return "Perfect Agreement"
    else:
        return "Invalid Accuracy"
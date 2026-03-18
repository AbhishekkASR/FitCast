import os
import sys
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.model_loader import extract_features

dataset = "dataset/fashion_images"

features = []
paths = []

for img in os.listdir(dataset):

    path = os.path.join(dataset, img)

    try:
        feature = extract_features(path)

        features.append(feature)
        paths.append(path)

    except:
        pass

os.makedirs("embeddings", exist_ok=True)

pickle.dump((features, paths), open("embeddings/features.pkl", "wb"))

print("Embeddings generated successfully")

import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from backend.model_loader import extract_features

features, paths = pickle.load(open("embeddings/features.pkl","rb"))

features = np.array(features)

def recommend(img_path, top_k=5):

    query = extract_features(img_path)

    similarity = cosine_similarity([query], features)[0]

    indices = np.argsort(similarity)[::-1][:top_k]

    results = []

    for i in indices:

        results.append(paths[i])

    return results
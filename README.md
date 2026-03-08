# 👕 FitCast – AI Fashion Recommendation System

FitCast is an AI-powered fashion recommendation system that suggests visually similar clothing items based on an uploaded outfit image.
The system uses **Deep Learning, Computer Vision, FastAPI, and Streamlit** to build a complete end-to-end AI web application.

This project demonstrates how to integrate a machine learning model with REST APIs and a web interface for real-time recommendations.

---

## 🚀 Features

* Image-based fashion recommendation
* Deep learning feature extraction using ResNet50
* Similarity search using cosine similarity
* FastAPI backend for real-time inference
* Streamlit frontend for interactive UI
* Embedding-based fast recommendation
* Supports large dataset with optimized storage
* Ready for cloud deployment

---

## 🧠 Tech Stack

| Category   | Tools                                 |
| ---------- | ------------------------------------- |
| Language   | Python                                |
| ML / CV    | TensorFlow, ResNet50                  |
| Backend    | FastAPI, Uvicorn                      |
| Frontend   | Streamlit                             |
| Libraries  | NumPy, Scikit-learn, Pillow, Requests |
| Deployment | Render, Streamlit Cloud               |

---

## 🏗️ System Architecture

User Upload Image
↓
Streamlit Frontend
↓
FastAPI Backend
↓
TensorFlow Feature Extraction
↓
Embedding Similarity Search
↓
Recommended Fashion Images

---

## 📁 Project Structure

```
FitCast
│
├── backend
│   ├── main.py
│   ├── recommender.py
│   ├── model_loader.py
│   ├── product_api.py
│
├── frontend
│   ├── app.py
│
├── training
│   ├── generate_embeddings.py
│
├── dataset
│   └── fashion_images      (not uploaded to GitHub)
│
├── embeddings
│   └── features.pkl        (generated locally)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

Dataset used:

Fashion Product Images Dataset (Kaggle)

Download link:

https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small

Details:

* Total images used: ~3500
* Dataset size: ~46 MB
* Used for similarity-based recommendation

After downloading, place images in:

```
dataset/fashion_images
```

Dataset is not uploaded to GitHub to keep repository small.

---

## ⚙️ Installation

Clone repository

```
git clone https://github.com/AbhishekkASR/FitCast.git
cd FitCast
```

Install dependencies

```
pip install -r requirements.txt
```

---

## 🔧 Generate Embeddings

Run once after adding dataset

```
python training/generate_embeddings.py
```

This will create:

```
embeddings/features.pkl
```

Embeddings store feature vectors for fast similarity search.

---

## ▶️ Run Backend

```
python -m uvicorn backend.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

API Docs

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

Open new terminal

```
cd frontend
python -m streamlit run app.py
```

Open in browser

```
http://localhost:8501
```

Upload an image to get recommendations.

---

## ⚠️ Notes

* Dataset and embeddings are ignored using `.gitignore`
* This keeps the repository small
* Embeddings must be generated locally before running

---

## 📈 Future Improvements

* FAISS for faster similarity search
* YOLO for clothing detection
* Real e-commerce API integration
* User preference learning
* Full cloud deployment

---

## 👨‍💻 Author

Abhishek Singh
B.Tech Computer & Communication Engineering
Manipal University Jaipur

GitHub
https://github.com/AbhishekkASR

---

## 📜 License

This project is for educational and research purposes.

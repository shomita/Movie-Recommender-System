# 🎬 Movie Recommender System

A simple **Movie Recommendation System** built using **Python, Machine Learning (NLP + Cosine Similarity)** and deployed with **Streamlit Cloud**.  
This app suggests movies similar to the one selected by the user.

---

## 🚀 Features
- Select any movie and get **top recommendations**.
- Uses **content-based filtering** with **cosine similarity**.
- Clean and interactive UI built with **Streamlit**.
- Deployed online and accessible via a public link.

---

## 🛠️ Tech Stack
- **Python**
- **Pandas & NumPy**
- **scikit-learn**
- **Pickle** (for saving trained model)
- **Streamlit** (for web app)

---

## 📂 Project Structure
movies/
│
├── app.py # Main Streamlit app
├── movies.pkl # Preprocessed movies data
├── similarity.pkl # Cosine similarity matrix
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## ▶️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Movie-Recommender-System.git
   cd Movie-Recommender-System
python -m venv .venv
.venv\Scripts\activate     # On Windows
source .venv/bin/activate  # On Mac/Linux
pip install -r requirements.txt
streamlit run app.py

🌐 Live Demo

The app is live here:
👉 Movie Recommender System on Streamlit : https://movie-recommender-system-evjnnfgrxnmppan2dwknyd.streamlit.app/



# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System that suggests similar movies based on features like genre, keywords, cast, and overview.

---

## 🚀 Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) techniques to recommend movies based on their similarity.

The system analyzes movie metadata and finds similar movies using cosine similarity.

---

## 🧠 How It Works

1. Load movie and credits datasets  
2. Merge datasets  
3. Select important features:
   - genres
   - keywords
   - cast
   - crew
   - overview  
4. Clean and preprocess data  
5. Extract important information (e.g., director from crew)  
6. Combine all features into a single column called `tags`  
7. Convert text into vectors using CountVectorizer  
8. Compute similarity using cosine similarity  
9. Recommend top 5 similar movies  

---

## 📊 Dataset

- TMDB 5000 Movies Dataset  
- Contains 4800+ movies  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## 🎯 Features

- Recommend similar movies  
- Fast similarity computation  
- Clean and interactive UI  
- Real-world ML pipeline  

---

## 💻 How to Run

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run src/main.py

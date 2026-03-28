# 🎬 Movie Recommendation System

An AI-powered Movie Recommendation System that suggests similar movies using both:
- Traditional NLP (CountVectorizer + Cosine Similarity)
- Transformer-based embeddings (SentenceTransformers)

Built with Python and deployed using Streamlit.

---

## 🚀 Project Overview

This project builds a **Content-Based Recommendation System** that analyzes movie metadata such as genres, keywords, cast, and overview to recommend similar movies.

The system was enhanced باستخدام **Transformer models** to capture semantic meaning between movies, not just keyword matching.

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**:

🔗 https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Files used:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 🧠 Data Preprocessing (Detailed)

After loading the datasets, we performed the following steps:

### 1️⃣ Merging Datasets
- Merged `movies` and `credits` on the `title` column

---

### 2️⃣ Selected Columns (IMPORTANT)

We selected only the most relevant features for recommendation:

- `movie_id` → unique identifier  
- `title` → movie name  
- `overview` → movie description (very important for NLP)  
- `genres` → type of movie (Action, Comedy, etc.)  
- `keywords` → important tags  
- `cast` → actors  
- `crew` → used to extract **director**

---

### 3️⃣ Handling Missing Values
- Filled missing values with empty strings
- Removed null rows

---

### 4️⃣ Feature Engineering

#### ✔ Convert JSON-like columns
Used `ast.literal_eval` to convert:
- genres
- keywords
- cast
- crew

From string → list of values

---

#### ✔ Extract Director
- Extracted only the **Director** from the `crew` column

---

#### ✔ Clean Text
- Removed spaces inside names:
  - `"Tom Cruise"` → `"TomCruise"`

👉 This prevents wrong tokenization later

---

#### ✔ Process Overview
- Split text into words

---

#### ✔ Create Final Feature (Tags)

Combined all features into one column:

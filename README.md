# 📚 Collaborative Filtering Book Recommender System

**Live demo:** https://pratik-book-recommender.streamlit.app/

![Book recommender app](Screenshot%202026-09-10%20180952.png)

An end-to-end Machine Learning web application that recommends books based on user reading history and ratings using item-based collaborative filtering. Built with **Scikit-Learn**, **Pandas**, and deployed via **Streamlit**.

---

## 📌 Project Overview

This project implements an item-based collaborative filtering recommender engine using the **Book-Crossing Dataset**. By constructing a sparse user-item interaction matrix and utilizing unsupervised **Nearest Neighbors (Cosine Distance / Brute Force)**, the system identifies and recommends books similar to a user's selection along with their cover posters.

---

## ✨ Features

- **Collaborative Filtering:** Generates recommendations derived from high-volume reader patterns and preferences.
- **Noise Reduction & Data Pruning:** Filters active users (>200 ratings) and popular books (≥50 ratings) to combat data sparsity.
- **Sparse Matrix Representation:** Uses `scipy.sparse.csr_matrix` for memory-efficient computation.
- **Dynamic Poster Fetching:** Automatically displays official cover art for recommended titles.
- **Interactive UI:** Clean Streamlit dashboard for real-time querying.

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (`NearestNeighbors`), SciPy (`csr_matrix`)
- **Web Framework:** Streamlit
- **Model Serialization:** Pickle

---

## 📂 Project Structure

```text
├── artifacts/
│   ├── model.pkl               # Fitted NearestNeighbors model
│   ├── books_name.pkl          # Index of filtered book titles
│   ├── final_rating.pkl        # Cleaned ratings metadata (with poster URLs)
│   └── book_pivot.pkl          # User-item pivot table
├── Book_Recommendor.ipynb      # Data cleaning and model training notebook
├── app.py                      # Streamlit application script
├── setup.py                    # Package distribution configuration
├── setup.sh                    # Streamlit server setup for deployment
├── Procfile                    # Cloud deployment orchestration
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 🚀 Run it locally

```bash
git clone https://github.com/pratiksinghds/book-recommender-system.git
cd book-recommender-system
pip install -r requirements.txt
streamlit run app.py
```

The trained model and lookup tables are already in `artifacts/`. The notebook `Book_Recommendor.ipynb` shows the data cleaning and model training.

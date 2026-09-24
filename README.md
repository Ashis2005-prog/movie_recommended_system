# 🎬 Movie Recommender System

A content-based movie recommendation web app built with **Python**, **scikit-learn**, **Pickle** and **Streamlit**. Pick a movie you like and the app suggests similar movies based on their content (genres, keywords, cast, crew and overview).

🔗 **Live Demo:** [Add your deployed app link here](https://your-app-link.com)

---

## 📌 Features

- Content-based recommendations using cosine similarity
- Simple, interactive web interface built with Streamlit
- Fast loading with pre-computed data stored as pickle files
- Ready to deploy on Heroku (`Procfile` and `setup.sh` included)

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3 |
| Machine Learning | scikit-learn (CountVectorizer, cosine similarity) |
| Data Handling | Pandas, NumPy |
| Serialization | Pickle |
| Web App | Streamlit |
| Deployment | Heroku |

---

## 🧠 How It Works

1. **Data collection** – A movie dataset (title, overview, genres, keywords, cast, crew) is loaded and cleaned.
2. **Feature engineering** – Important columns are merged into a single `tags` column for every movie.
3. **Vectorization** – The tags are converted into numerical vectors using `CountVectorizer`.
4. **Similarity calculation** – Cosine similarity is computed between all movie vectors.
5. **Serialization** – The processed movie data and similarity matrix are saved using `pickle`.
6. **Recommendation** – When a user selects a movie, the app finds the most similar movies from the similarity matrix and shows the top results.

---

## 📁 Project Structure

```
movie_recommended_system/
│
├── Movie-Recommended-System.ipynb   # Data processing & model building notebook
├── app.py                           # Streamlit web application
├── requirements.txt                 # Python dependencies
├── Procfile                         # Heroku process file
├── setup.sh                         # Streamlit configuration for deployment
├── .gitignore                       # Files ignored by Git
└── README.md                        # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ashis2005-prog/movie_recommended_system.git
cd movie_recommended_system
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the pickle files

Open and run all cells in `Movie-Recommended-System.ipynb`. This creates the pickle files (movie data and similarity matrix) that `app.py` needs.

### 5. Run the app

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

---

## ☁️ Deployment (Heroku)

This project includes the files needed for Heroku deployment:

- `Procfile` – tells Heroku how to start the app
- `setup.sh` – creates the Streamlit config for the server

```bash
heroku login
heroku create your-app-name
git push heroku main
```

---

## 📷 Screenshots

_Add screenshots of your app here._

```markdown
![App Screenshot](screenshots/home.png)
```

---

## 🔮 Future Improvements

- Show movie posters using the TMDB API
- Add filters by genre, year or rating
- Try TF-IDF or embedding-based similarity for better results
- Add user-based collaborative filtering

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, create a branch and open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

---

## 👤 Author

**Ashis**
GitHub: [@Ashis2005-prog](https://github.com/Ashis2005-prog)

---

⭐ If you found this project useful, please give it a star!


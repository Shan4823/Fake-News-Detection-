
## 📰 Fake News Detection Using Machine Learning

A web-based **Fake News Detection** system built using **Python**, **Flask**, and **Machine Learning**.
The application predicts whether a given news article is *real* or *fake* based on its textual content.

---

### 🚀 Features

* 🧠 Machine Learning model trained on labeled news data
* 🔍 Predicts fake or real news from input text
* 💾 Pre-trained model (`PCL.pkl`) and vectorizer (`vectorizer.pkl`) included
* 🌐 Flask web interface for easy interaction
* 📊 Jupyter Notebook (`PCL.ipynb`) for model training and evaluation

---

### 🛠️ Tech Stack

* **Programming Language:** Python
* **Framework:** Flask
* **Libraries:** scikit-learn, pandas, numpy, pickle
* **Frontend:** HTML/CSS (via Flask templates)
* **Dataset:** `news.csv` (contains labeled real/fake news data)

---

### 📂 Project Structure

```
Fake News Detection/
├── app.py                # Flask app entry point
├── PCL.ipynb             # Jupyter notebook for model training/testing
├── PCL.pkl               # Trained ML model
├── vectorizer.pkl        # Fitted text vectorizer (TF-IDF or CountVectorizer)
├── news.csv              # Dataset for training and evaluation
├── requirements.txt      # Python dependencies
├── .gitattributes
└── README.md
```

---

### ⚙️ Setup & Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Fake-News-Detection.git
cd Fake-News-Detection
```

#### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the Flask Application

```bash
python app.py
```

The app will run on **`http://localhost:5000`** 🌐

---

### 🧠 Model Training (Optional)

If you want to retrain or tweak the model:

1. Open `PCL.ipynb` in Jupyter Notebook.
2. Run all cells to preprocess data, train the model, and save new `.pkl` files.
3. Replace the existing `PCL.pkl` and `vectorizer.pkl` files.

---

### 📊 Example Usage

**Input:**

> "Breaking: Scientists discover water on Mars!"

**Output:**
✅ Real News
or
❌ Fake News

---

### 💡 Future Enhancements

* 🧩 Add API endpoints for integration with other systems
* ☁️ Deploy on Render / AWS / Heroku
* 📱 Build a React frontend for better UI
* 🔐 Add user authentication and saved history

---

### 👨‍💻 Author

**Shantanu Raj**


Would you like me to enhance this README with **deployment steps (e.g., Render or Heroku)** or keep it focused only on **local setup**?

```markdown
#  Cryptocurrency Liquidity Predictor

A machine learning web application built with **Flask** that predicts the **liquidity ratio** of a cryptocurrency coin using market features like price, volume, and volatility. It also classifies coins into **Low**, **Medium**, or **High Liquidity** to help traders and platforms make informed decisions.

---

##  Live Demo

> [Coming Soon] Deployed via [Render](https://render.com/)

---

##  What is Liquidity Ratio?

**Liquidity Ratio = 24h Volume / Market Capitalization**

It indicates how actively a coin is traded. A higher ratio means the asset is easier to buy/sell without major price impact — critical for market stability.

---

##  Features

-  Predicts liquidity ratio from 7 key market features
-  Classifies output into **Low**, **Medium**, or **High Liquidity**
-  Clean Flask-based web UI
-  Ready for deployment on Render, Heroku, or local machine

---

##  Technologies Used

| Tool         | Purpose                     |
|--------------|-----------------------------|
| Flask        | Web framework               |
| scikit-learn | Base ML models              |
| XGBoost      | Advanced regression model   |
| HTML/CSS     | Frontend with Jinja2        |
| joblib       | Save/load trained model     |

---

##  Project Structure

```

crypto-liquidity-app/
├── app.py                          # Flask backend
├── final\_liquidity\_stack\_model.pkl # Trained ML model
├── requirements.txt               # Dependencies
├── templates/
│   └── index.html                 # Web form UI
├── .gitignore                     # Ignored files
└── README.md                      # This file

````

---

##  Sample Input to Test

| Field            | Value           |
|------------------|-----------------|
| Price            | `2750.50`       |
| 1h % Change      | `0.02`          |
| 24h % Change     | `0.08`          |
| 7d % Change      | `0.12`          |
| 24h Volume       | `18500000000`   |
| Market Cap       | `325000000000`  |
| Volatility Score | `0.073`         |

> Expected Output:
> - Predicted Liquidity Ratio: `~0.12`
> - Classification: `Medium`

---

##  Model Details

- **Model Type**: Stacking Regressor
- **Base Learners**: Random Forest, XGBoost, SVR
- **Meta Learner**: Linear Regression
- **Target**: Log-transformed liquidity ratio
- **Performance**: R² Score ~0.95 (excellent fit)

---

##  How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/Naveen-jangid/crypto-liquidity-app.git
cd crypto-liquidity-app
````

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🌐 Deployment on Render (Optional)

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Create New → Web Service
3. Connect this GitHub repo
4. Set:

   * **Build command**: `pip install -r requirements.txt`
   * **Start command**: `python app.py`
   * **Environment**: Python 3.10+, Port 5000
5. Deploy!

---

## 🙋 Author

**Naveen Jangid**
📧 [naveen@example.com](nvnjan95@gmail.com)
🔗 [GitHub](https://github.com/Naveen-jangid)

---

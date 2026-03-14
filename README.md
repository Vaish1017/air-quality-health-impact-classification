# 🌍 Air Quality Health Impact Prediction

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **Machine Learning powered web application** that predicts the **health risk caused by air pollution** using environmental and pollution indicators.

This project demonstrates a **complete end-to-end data science workflow**, including:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Machine learning model development
* Model evaluation
* Deployment using **Streamlit**

The application allows users to **input air quality parameters and instantly receive a predicted health impact class.**

---

# 🚀 Live Application

🔗 **Deployment Link**

https://air-quality-health-impact-classification-bkipnnphaeazqq8kjhzza.streamlit.app/


---

# 📌 Project Highlights

 * End-to-End Machine Learning Pipeline
 * Interactive Web App using **Streamlit**
 * Pollution Feature Analysis with **EDA**
 * Real-time Health Risk Prediction
 * Clean UI with user-friendly controls

---

# 🧠 Problem Statement

Air pollution is one of the **leading environmental health risks worldwide**, affecting millions of people every year.

Pollutants such as:

* **PM2.5**
* **PM10**
* **Nitrogen Dioxide (NO₂)**
* **Sulfur Dioxide (SO₂)**
* **Ozone (O₃)**

can significantly impact **respiratory and cardiovascular health**.

The goal of this project is to:

* Analyze environmental and pollution indicators
* Train a machine learning model to predict **health impact risk**
* Provide an **interactive web interface** for predictions

---

# 📊 Dataset Overview

The dataset contains **environmental and pollution indicators** used to predict a **Health Impact Class**.

### Features

| Feature     | Description                           |
| ----------- | ------------------------------------- |
| AQI         | Air Quality Index                     |
| PM2.5       | Fine particulate matter concentration |
| PM10        | Particulate matter ≤10 µm             |
| NO2         | Nitrogen dioxide concentration        |
| SO2         | Sulfur dioxide concentration          |
| O3          | Ozone concentration                   |
| CO          | Carbon monoxide concentration         |
| Temperature | Ambient temperature                   |
| Humidity    | Relative humidity                     |
| WindSpeed   | Wind speed                            |
| Pressure    | Atmospheric pressure                  |
| Visibility  | Air visibility                        |

---

### 🎯 Target Variable

**HealthImpactClass**

Possible output classes:

* Low Risk
* Moderate Risk
* High Risk

---

# ⚙️ Machine Learning Pipeline

The project follows a structured **Data Science workflow**.

---

## 1️⃣ Data Preprocessing

Data cleaning and preparation steps include:

* Handling missing values
* Removing duplicate records
* Feature scaling
* Train-test split

Libraries used:

```
pandas
numpy
scikit-learn
```

---

## 2️⃣ Exploratory Data Analysis (EDA)

EDA helps identify **patterns and relationships** in pollution indicators.

Key analysis includes:

* Distribution plots
* Outlier detection using boxplots
* Class distribution analysis
* Correlation heatmaps

Libraries used:

```
matplotlib
seaborn
```

---

## 3️⃣ Model Training

Multiple machine learning algorithms can be trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting

The trained model is saved using:

```
joblib
```

---

# 📈 Model Evaluation

The model is evaluated using standard **classification metrics**:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Example performance:

```
Accuracy : 0.89
F1 Score : 0.87
```

---

# 🖥️ Streamlit Web Application

A fully interactive **Streamlit web app** was built to make predictions easily.

### Application Features

✔ User input sliders
✔ Clean and responsive UI
✔ Instant predictions
✔ Real-time ML inference

Run locally:

```
python -m streamlit run app.py
```

---

# 📂 Project Structure

```
Air-Quality-Health-Impact-Prediction
│
├── data
│   └── air_quality_dataset.csv
│
├── notebooks
│   └── Final.ipynb
│
├── models
│   └── trained_model.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 🔧 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Vaish1017/air-quality-health-impact-classification.git
```

### 2️⃣ Navigate to the project directory

```
cd air-quality-health-impact-classification
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the Streamlit app:

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 🏗️ Tech Stack

| Category             | Tools               |
| -------------------- | ------------------- |
| Programming Language | Python              |
| Data Analysis        | Pandas, NumPy       |
| Data Visualization   | Matplotlib, Seaborn |
| Machine Learning     | Scikit-learn        |
| Model Deployment     | Streamlit           |

---

# 🔮 Future Improvements

Potential upgrades for the project:

* Deploy with **Streamlit Cloud**
* Integrate **real-time air quality APIs**
* Add **interactive pollution maps**
* Implement **advanced ML models**
* Create a **live monitoring dashboard**

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make improvements
4. Submit a pull request

---

# 👩‍💻 Author

**P Vaishnavi**

Aspiring **Data Scientist | Machine Learning Enthusiast**

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to:

* Use
* Modify
* Distribute

with proper attribution.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share it with others

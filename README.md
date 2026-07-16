# 📚 Student Performance Prediction

An end-to-end Machine Learning project that predicts a student's **Math Score** based on demographic, educational, and academic factors. The project includes data preprocessing, model training, a Flask web application, and deployment on Render.

---

## 🚀 Live Demo

🌐 **Web App:**  
https://student-performance-prediction-2-hh0a.onrender.com/

---

## 📌 Project Overview

Student academic performance is influenced by several factors such as parental education, lunch type, preparation courses, and previous academic scores.

This project uses Machine Learning to predict a student's **Math Score** using these features. The complete ML pipeline is implemented, from data ingestion to deployment.

---

## 🎯 Problem Statement

Predict a student's **Math Score** based on:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The model can help understand the relationship between various educational factors and student performance.

---

## 📊 Dataset Features

| Feature | Description |
|----------|-------------|
| Gender | Student Gender |
| Race/Ethnicity | Student Group |
| Parental Level of Education | Highest education level of parents |
| Lunch | Standard or Free/Reduced |
| Test Preparation Course | Completed / None |
| Reading Score | Reading marks |
| Writing Score | Writing marks |
| Math Score | Target Variable |

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- Render
- Pickle

---

## 🧠 Machine Learning Workflow

- Data Ingestion
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Selection
- Prediction Pipeline
- Flask Web Application
- Deployment on Render

---

## 📂 Project Structure

```
Student-Performance-Prediction/
│
├── artifacts/
├── notebook/
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
│
├── templates/
│   ├── home.html
│
│
├── app.py
├── requirements.txt
├── setup.py
├── README.md
```

---

## 📈 Model Performance

Multiple regression algorithms were trained and evaluated.

The best-performing model was selected based on evaluation metrics such as:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 💻 Running the Project Locally

### Clone the Repository

```bash
git clone https://github.com/Diksha-ydv/Student-Performance-Prediction
```

### Navigate to the Project

```bash
cd Student-Performance-Prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

The application is deployed using:

- Flask
- Render

---

## 📦 Dataset

The dataset used in this project is the **Students Performance in Exams** dataset available on Kaggle.

**Dataset Link:**

https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

---

## ⭐ Future Improvements

- Improve UI/UX
- Add Model Explainability
- Deploy using Docker
- Add User Authentication
- Add Batch Prediction
- Integrate Database Support

---

## 👩‍💻 Author

**Diksha Yadav**

LinkedIn: www.linkedin.com/in/diksha-yadav06

GitHub: https://github.com/Diksha-ydv

---

## 📄 License

This project is created for educational and portfolio purposes.

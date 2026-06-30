# Smart Water Level Control System using Machine Learning with Python

## Overview

The Smart Water Level Control System is a web-based application developed using Python and Flask. It monitors the water level in a storage tank and controls the motor efficiently. The project also demonstrates the use of Machine Learning to predict motor operation based on water level data.

## Features

- Water Level Monitoring
- Tank Level Visualization
- Motor ON/OFF Control
- Auto Mode
- Manual Mode
- Dashboard Interface
- Water Alerts
- System Health Status
- Power Status
- Water Usage History
- Machine Learning Prediction

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Pandas
- Scikit-learn
- Joblib

## Machine Learning Algorithm

**Decision Tree Classifier**

The model is trained using sample water level data to predict whether the water motor should be turned ON or OFF automatically.

## Project Structure

```
Smart-Water-Level-Control-System/
│
├── app.py
├── train_model.py
├── water_usage.csv
├── water_model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/Smart-Water-Level-Control-System.git
```

2. Open the project folder.

```bash
cd Smart-Water-Level-Control-System
```

3. Install the required libraries.

```bash
python -m pip install flask pandas scikit-learn joblib
```

4. Train the Machine Learning model.

```bash
python train_model.py
```

5. Run the Flask application.

```bash
python app.py
```

6. Open your browser and visit:

```
http://127.0.0.1:5000
```

## Workflow

1. Read water level data.
2. Train the Machine Learning model.
3. Save the trained model.
4. Load the model in the Flask application.
5. Predict motor status.
6. Display the result on the dashboard.

## Advantages

- Reduces water wastage.
- Prevents tank overflow.
- Saves electricity.
- Easy to monitor water level.
- Supports automatic motor control.

## Future Scope

- IoT Sensor Integration
- Mobile Application
- Cloud Deployment
- SMS/Email Alerts
- Real-time Sensor Monitoring

## Conclusion

This project demonstrates the integration of Python, Flask, and Machine Learning to develop an intelligent water level monitoring and motor control system. It helps improve water management and reduce manual effort.

## Author

**Keerthi Mandava**

Machine Learning with Python Internship Project

# BMI Calculator (PyQt)

A simple BMI (Body Mass Index) calculator built with PyQt.

## Features

- Metric and Imperial input modes
- BMI calculation: `BMI = Weight(kg) / (Height(m))²`
- BMI status: Underweight, Normal, Overweight, Obese
- Menu bar:
  - **File → Clear** clears inputs
  - **File → Exit** closes the app
  - **Help → How to use** shows instructions

## How to run

### 1) Install dependencies

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2) Start the app

```bash
python main.py
```

## Sample input / output

### Example 1 (Metric)
- Weight: **70**
- Height: **1.75**
- Output:
  - BMI: **22.86**
  - Status: **Normal**

### Example 2 (Imperial)
- Weight: **200**
- Height: **70**
- Output:
  - BMI: **28.70**
  - Status: **Overweight**

## Screenshots

![Metric example](screenshots/metric_example.png)

![Imperial example](screenshots/imperial_example.png)

# Employee-Leave-Assistant
A Python and Flask-based Employee Leave Assistant that calculates employee leave days by automatically excluding weekends and predefined company holidays, with date validation and a simple web interface.
# Employee Leave Assistant

A simple web-based Employee Leave Assistant built using Python and Flask. It helps employees calculate their leave duration based on a selected date range.

The application automatically identifies working days, weekends, and predefined company holidays to calculate the total leave days.

## Features

- Calculate leave duration between two dates.
- Automatically exclude Saturdays and Sundays.
- Exclude predefined company holidays.
- Validate date formats and date ranges.
- Display calendar days, leave days, weekends, and holidays separately.
- Simple and user-friendly web interface.
- Prevent calculations outside the supported year (2026).

## Technologies Used

- **Python** – Core programming language.
- **Flask** – Web application framework.
- **HTML5** – Frontend structure.
- **CSS3** – User interface styling.
- **datetime** – Date validation and calculations.

## Project Structure

```text
Employee-Leave-Assistant/
│
├── app.py
├── tools.py
├── test_tool.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── leave_categories.txt
│   ├── leave_procedure.txt
│   └── working_calendar.txt
│
└── templates/
    └── index.html
```

## How It Works

1. The employee selects a start date and end date.
2. Flask receives the submitted dates.
3. The application validates the date format and supported year.
4. The calculation function checks each date in the selected range.
5. Saturdays and Sundays are counted as weekend days.
6. Predefined company holidays falling on weekdays are counted separately.
7. Remaining weekdays are counted as leave days.
8. The results are displayed on the web page.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Employee-Leave-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

```text
http://127.0.0.1:5000
```

## Testing

Run the test file using:

```bash
python test_tool.py
```

The tests validate:
- Normal leave calculations.
- Company holiday calculations.
- Invalid date ranges.
- Unsupported years.

## Limitations

- Currently supports dates within 2026 only.
- Company holidays are predefined in the Python code.
- Does not submit leave applications.
- Does not approve or reject leave requests.
- Does not connect to an HR management system.

## Future Improvements

- Support multiple calendar years.
- Store company holidays in a database.
- Add employee login and authentication.
- Integrate leave balance tracking.
- Add leave application submission.
- Introduce HR approval workflows.

## Disclaimer

This application is designed for leave-day calculation and informational purposes. It does not replace official company leave policies or HR approval procedures.

---

**Developed using Python and Flask.**

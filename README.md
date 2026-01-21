# HR Analytics Dashboard

**Solutions by STC – Workforce Insights**

---

##  Project Overview

The **HR Analytics Dashboard** is designed to help HR teams, managers, and decision-makers understand workforce data quickly and clearly.

Instead of working with large spreadsheets or raw datasets, the dashboard transforms employee data into **clear metrics and visual insights**, all presented on a **single, easy-to-read interface**.

The dashboard answers key HR questions related to **employee count, attrition, performance, income, and tenure**, enabling faster and more informed decision-making.

---

##  Why This Dashboard Matters

HR departments often work with complex and large datasets. This dashboard simplifies that process by:

* Converting raw employee data into **meaningful insights**
* Highlighting potential **risk areas**, such as high attrition
* Supporting **strategic HR decision-making**
* Saving time by presenting everything in **one unified view**

The dashboard is intentionally designed to be understandable for **non-technical users**, including managers and executives.

---

##  What Does the Dashboard Show?

### 1. Executive Overview

A high-level snapshot of workforce health, including:

* Total number of employees
* Attrition rate
* Average monthly income
* Average performance rating

This section allows leadership to quickly assess the overall state of the organization.

---

### 2. Workforce and Attrition Insights

Visual analytics showing:

* Employee distribution across departments
* Attrition risk by department
* Performance rating distribution

These visuals help identify patterns, trends, and potential issues without deep technical analysis.

---

### 3. Compensation and Workforce Trends

Long-term workforce insights, including:

* Income distribution across departments
* Employee tenure trends

These insights support understanding of **salary structures** and **employee retention behavior**.

---

##  Data Interaction Features

The dashboard supports basic HR operations directly from the interface:

### Add a New Employee

* HR staff can add new employee records through the dashboard.

### Update Employee Income

* HR staff can update the salary of existing employees.

All changes are:

* Saved permanently
* Reflected immediately in the dashboard

---

##  Data Storage

Employee data is stored in a **local database file**, ensuring that:

* Data persists after the application is closed
* Newly added employees remain saved
* Salary updates are preserved

Each time the dashboard runs, it loads the **most up-to-date data** from the database.

---

##  Target Users

This dashboard is suitable for:

* HR teams
* Department managers
* Business stakeholders
* Executives seeking high-level workforce insights

It is built for **clarity, speed, and practical use**.

---

##  Design Approach

The dashboard follows professional business and analytics design standards:

* One-page layout for clear visibility
* Soft background colors with white content sections
* Clean, minimal visuals focused on insight rather than complexity
* Color palette aligned with **Solutions by STC** branding

**Design goal:** clarity over complexity.

---

##  Project Structure

The project consists of two main components:

### 1. Data Analysis Notebook

* Jupyter Notebook for data exploration, cleaning, and analysis.

### 2. Dashboard Application

* Python application that displays the interactive dashboard and visualizations.

---

##  Technical Information

### Languages

* Python
* SQL

### Tools & Technologies

* Data analysis and processing
* Local database storage
* Interactive web-based dashboard (Streamlit)

---



##  How to Run the Dashboard

1. Activate the Python environment
2. Navigate to the project folder
3. Install required dependencies
 ```bash
   pip install -r requirements.txt
  ```
4. Run the application:

```bash
streamlit run app.py
```

5. Open the dashboard in your browser:

```
http://localhost:8501
```

---

##  Summary

The **HR Analytics Dashboard** converts employee data into **actionable insights**.

It helps organizations to:

* Understand their workforce clearly
* Identify potential risks early
* Support better HR and business decisions
* Access all key workforce information in one place

---

##  Author

**Name:** Lina Alnasi
**Role:** Software Engineering Student (Artificial Intelligence & Data Science)
**Project Type:** HR Data Analytics Dashboard
**Purpose:** Academic and practical data analytics project

---

 *This project demonstrates practical HR analytics, dashboard design, and data-driven decision support aligned with real-world business needs.*

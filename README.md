# 💼 Expense Tracking App for Hostel Students

A full-stack web application built to help hostel students track daily expenses, manage shared costs, and stay on top of payments — improving financial awareness and reducing money-related stress.

---

##  Table of Contents

- [💡 Motivation](#-motivation)
- [Demo](#-demo)
- [Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✅ Challenges](#-challenges)
- [🌟 Impact](#-impact)
- [⚙️ Technologies Used](#-technologies-used)
- [🛠️ Features](#features)
- [📦 Setup Instructions](#setup-instructions)
- [☁️ Streamlit Deployment](#streamlit-deployment)
- [📁 Project Structure](#project-structure)
- [👥 Student Contributions & Roles](#student-contributions--roles)
- [🏢 Internship Info](#internship-info)


## 💡 Motivation

Managing personal finances is a crucial skill, yet many hostel students struggle with it. With limited monthly allowances and multiple shared and personal expenses like food, laundry, and college dues, students often lose track of where their money goes.

Existing finance apps are often cluttered, business-focused, or not user-friendly for students. There was a need for a **simple, lightweight, and student-centric solution** that helps track daily spending, manage group costs, and build better financial habits — all without requiring advanced tech skills.

This project was developed to **empower students with financial clarity**, reduce end-of-month stress, and promote smarter budgeting through an intuitive and interactive platform.


## Demo
<img src="Tab1" width="500"/>
  <img src="Tab2" width="500"/>
  <img src="Tab3" width="600"/>

---

##  Overview

This project was developed during a 6-week offline internship at **Pixel Mind Solutions Pvt. Ltd**, Hyderabad.  
The application simplifies expense tracking for hostel students by allowing:

- Daily tracking of personal and group expenses  
- Clear visibility into spending categories  
- Notifications for due payments  
- An interactive and clean UI built with Streamlit

---

## 🎯 Problem Statement

Hostel students often struggle to manage their monthly budgets due to:

- No clear tracking of where money is spent  
- Missing dues for mess/laundry/college fees  
- No support for shared/group expenses  
- Traditional apps not focused on student needs

---

##  Challenges

- Lack of visibility into daily expenditures  
- No built-in alerts for due payments  
- Manual management of shared expenses  
- Complex or cluttered financial apps

---

##  Impact

- Helps reduce financial stress  
- Encourages savings & better planning  
- Enhances focus by reducing money worries  
- Promotes responsible spending behavior

---

## Technologies Used

| Technology         | Purpose                            |
|--------------------|-------------------------------------|
| **MySQL**          | Secure expense data storage         |
| **FastAPI**        | Backend API development             |
| **Streamlit**      | Interactive frontend UI             |
| **Postman**        | API testing & debugging             |
| **Streamlit Cloud**| Web app deployment                  |

---

## Features

- Add and view daily expenses  
- Categorize by type (food, rent, travel, etc.)  
- Summarize monthly expenses  
- Real-time data sync with MySQL  
- Simple, mobile-friendly interface

---


## Setup-Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Balajiscientist/expense_management_system_for_hostel_students.git
   cd expense_management_system_for_hostel_students

   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run app.py
   ```

## streamlit-deployment

To deploy your application online using **Streamlit Cloud**:

1. **Push the code** to your GitHub repository.
2. Go to [**Streamlit Cloud**](https://streamlit.io/cloud).
3. **Create a new app** by connecting your GitHub repository.
4. Set `app.py` as the **entry point** of your application.
5. (Optional) **Add environment variables and secrets** (like database credentials) using the **Streamlit secrets manager**.

> Once deployed, your app will be accessible via a public URL provided by Streamlit Cloud.


## Project-Structure

- **frontend**: Contains the Streamlit application code.
- **backend**: Contains the FastAPI backend server code.
- **tests**: Contains the front and backend test cases.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Student Contributions & Roles

| Name                  | Role               | Key Contributions |
|-----------------------|--------------------|--------------------|
| **B. Balaji**         | Full Stack Developer | - Designed and integrated both frontend and backend  <br> - Managed database connectivity and API testing  <br> - Deployed the application on Streamlit Cloud |
| **K. Surya Akhil Varma** | Backend Developer     | - Built RESTful APIs using FastAPI  <br> - Handled secure data transfer and validation  <br> - Connected backend logic with MySQL database |
| **K. Yuva Sankar**    | Frontend Developer   | - Developed user-friendly interfaces using Streamlit  <br> - Designed intuitive UI/UX for student use  <br> - Created visual dashboards for expense insights |

---

## Internship Info

- **Company**: Pixel Mind Solutions Pvt. Ltd, Kukatpally, Hyderabad  
- **Supervisor**: Dr. S. Sangeetha, Dept. of CSE (AI & DS), The Apollo University  
- **Internship Duration**: May 1, 2025 – June 14, 2025  
- **Mode**: Offline  
- **Domain**: Full-Stack Development & Data Science  
- **Contact**: [info@pixelmindsolutions.com](mailto:info@pixelmindsolutions.com)  
- **Website**: [www.pixelmindsolutions.com](https://www.pixelmindsolutions.com)




   

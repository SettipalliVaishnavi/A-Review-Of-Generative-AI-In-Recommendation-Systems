# A Review Of Generative AI In Recommendation Systems

## 📌 Project Overview

This project is a Django-based web application that explores the use of Generative AI techniques in Recommendation Systems.

The application integrates the Google Gemini API to generate AI-based explanations, recommendations, technical insights, and improvement suggestions for different recommendation-system problems.

## 🎯 Objectives

- Understand the role of Generative AI in Recommendation Systems.
- Explore GANs and VAEs for generating synthetic recommendation data.
- Address the Cold Start Problem using Generative AI.
- Improve diversity in recommendation results.
- Analyze and improve recommendation-system architectures.
- Generate AI-based technical responses using Google Gemini API.

## 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- Google Gemini API
- SQLite
- xhtml2pdf
- python-dotenv

## 🤖 Generative AI Integration

The application uses the Google Gemini API to generate responses based on the selected recommendation-system task and the user's input.

### Workflow

**User Input → Django → Prompt Creation → Gemini API → AI Response → Web Page**

The Django backend creates a structured prompt and sends it to Gemini. Gemini processes the prompt and returns a Generative AI response, which is displayed to the user.

## ✨ Main Features

### 1. User Registration

Users can create an account through the registration page.

### 2. User Login

Registered users can log in and access the application.

### 3. AI Recommendation Tasks

Users can select different tasks:

- Generate Synthetic Recommendations using GANs/VAEs
- Address Cold Start Problem with GenAI Techniques
- Enhance Diversity in Recommendation Results
- Assess & Improve Recommendation System Architecture

### 4. Gemini AI Responses

Gemini generates detailed responses based on the selected task and user-provided context.

### 5. PDF Export

Users can export the generated AI response as a PDF.

### 6. Admin Management

The application contains an admin section for managing registered users and account activation.

## 🔄 Project Workflow

1. User opens the Django web application.
2. User registers an account.
3. User logs in using their credentials.
4. User selects a recommendation-system task.
5. User enters the problem description or context.
6. Django creates a structured prompt.
7. The prompt is sent to the Google Gemini API.
8. Gemini generates the response.
9. Django displays the response on the web page.
10. The user can download the generated response as a PDF.

## 🧠 Recommendation System Concepts

The project explores:

- Generative AI
- GANs
- VAEs
- Hybrid Models
- Transformers
- Collaborative Filtering
- Cold Start Problem
- Recommendation Diversity

## 📂 Project Structure

```text
A-Review-Of-Generative-AI-In-Recommendation-Systems/
│
├── Recommendation_Systems/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── admins/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── users/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── admin.py
│
├── templates/
│   ├── users/
│   └── admins/
│
├── static/
│   ├── gans_viz.png
│   └── vaes_viz.png
│
├── documentation.md
├── manage.py
└── .gitignore
```

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/SettipalliVaishnavi/A-Review-Of-Generative-AI-In-Recommendation-Systems.git
```

### 2. Open the Project Folder

```bash
cd A-Review-Of-Generative-AI-In-Recommendation-Systems
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install django google-genai python-dotenv xhtml2pdf
```

### 6. Configure the Gemini API Key

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_api_key_here
```

**Important:** Do not upload the `.env` file or expose your Gemini API key publicly.

### 7. Run Migrations

```bash
python manage.py migrate
```

### 8. Start the Django Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 📄 PDF Generation

The application uses `xhtml2pdf` to convert the generated AI response into a downloadable PDF document.

## 🔐 Security

Sensitive information such as the Gemini API key is stored in an environment variable and excluded from Git using `.gitignore`.

## 🚀 Future Enhancements

- Add more recommendation-system algorithms.
- Add recommendation-result visualizations.
- Add user history for generated responses.
- Add more Generative AI models.
- Improve recommendation evaluation metrics.
- Deploy the application to a cloud platform.

## 👩‍💻 Author

**Settipalli Vaishnavi**

B.Tech – Computer Science Engineering

GitHub:  
https://github.com/SettipalliVaishnavi

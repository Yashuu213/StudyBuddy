# CBSE Learning Website

A complete learning platform for Class 11 & 12 students with AI-powered doubt resolution and quiz generation.

## 🚀 Features
- **Comprehensive Curriculum**: Physics, Chemistry, and Maths for Class 11 & 12.
- **AI Doubt Assistant**: Powered by Google Gemini to answer questions in Board/JEE style.
- **Dynamic Content**: Explanations, Q&A, and Notes generated on demand.
- **Quiz Generator**: Test your knowledge with AI-generated quizzes.
- **Modern UI**: Dark theme with Glassmorphism design.

## 🛠️ Setup Instructions

### 1. Install Dependencies
Open a terminal in this folder and run:
```bash
pip install -r requirements.txt
```

### 2. Configure Gemini API Key
You need a Google Gemini API key.
- **Windows (PowerShell)**:
  ```powershell
  $env:GEMINI_API_KEY="your_api_key_here"
  ```
- **Windows (CMD)**:
  ```cmd
  set GEMINI_API_KEY=your_api_key_here
  ```
- **Linux/Mac**:
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  ```

### 3. Run the Application
```bash
python app.py
```

### 4. Access the Website
Open your browser and go to:
`http://127.0.0.1:5000`

## 📂 Project Structure
- `app.py`: Main Flask application (Backend).
- `data.json`: Curriculum hierarchy and dummy data.
- `templates/index.html`: Complete Frontend (HTML/CSS/JS).
- `requirements.txt`: Python dependencies.

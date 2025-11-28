# 🎓 StudyBuddy - AI Learning Companion

![StudyBuddy Banner](https://via.placeholder.com/1200x300/0f172a/38bdf8?text=StudyBuddy+AI+Learning+Companion)

**StudyBuddy** is a cutting-edge, AI-powered educational platform designed to revolutionize how students prepare for **CBSE** and **JEE** examinations. By combining a comprehensive curriculum with an intelligent **Gemini-powered AI Assistant**, StudyBuddy offers personalized learning, instant doubt resolution, and smart progress tracking.

---

## ✨ Key Features

### 🧠 Intelligent AI Companion
- **24/7 Doubt Resolution**: Ask any question related to your syllabus and get instant, accurate answers.
- **Context-Aware**: The AI understands which topic you are studying and provides relevant explanations.
- **Exam-Focused**: Get answers tailored for Board Exams (step-by-step) or JEE (conceptual shortcuts).

### 📚 Comprehensive Curriculum
- **Structured Content**: Organized by Class > Subject > Chapter > Topic.
- **Multi-Format Learning**:
    - **Explanations**: Deep dive into concepts.
    - **Board Q&A**: Practice with previous year questions.
    - **JEE Q&A**: Challenge yourself with competitive level problems.
    - **Notes**: Quick revision summaries.

### 🎯 Interactive Quizzes
- **Dynamic Generation**: Quizzes are generated on-the-fly by AI based on the specific topic.
- **Instant Feedback**: Get real-time scoring and detailed explanations for every answer.
- **Progress Tracking**: Your quiz scores are recorded to help you identify strengths and weaknesses.

### 🎨 Modern & Immersive UI
- **Glassmorphism Design**: A sleek, modern interface with dark mode support.
- **Hero Sections**: Engaging visual headers for every subject and chapter.
- **Responsive**: Works seamlessly on desktops, tablets, and mobile devices.

### 📈 Smart Progress & Settings
- **Dashboard**: Track your learning journey with visual progress bars.
- **Customization**: Personalize your experience (coming soon).

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript
- **Backend**: Python, Flask
- **AI Engine**: Google Gemini Pro (gemini-2.0-flash)
- **Data**: JSON-based structured curriculum

---

## 🚀 Getting Started

Follow these simple steps to set up StudyBuddy on your local machine.

### Prerequisites
- Python 3.8 or higher
- A Google Cloud Project with Gemini API access

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/studybuddy.git
    cd studybuddy
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key**
    - Open `app.py`.
    - Replace the placeholder with your actual Gemini API Key:
      ```python
      GEMINI_API_KEY = 'YOUR_ACTUAL_API_KEY'
      ```
    - *Note: For production, it is recommended to use environment variables.*

4.  **Run the Application**
    ```bash
    python app.py
    ```

5.  **Start Learning**
    - Open your browser and navigate to: `http://127.0.0.1:5000`

---

## 📖 Usage Guide

1.  **Select Your Class**: Choose between Class 11 or 12 from the Home page.
2.  **Navigate**: Pick a Subject, then a Chapter, and finally a Topic.
3.  **Learn**: Read the AI-generated explanations and notes.
4.  **Practice**: Switch tabs to view Board or JEE Q&A.
5.  **Test**: Click "Take Quiz" to test your understanding.
6.  **Ask**: Use the floating AI Chat button at the bottom right to clear any doubts instantly.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  Made with ❤️ for Students
</p>

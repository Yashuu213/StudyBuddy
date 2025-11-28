from flask import Flask, render_template, jsonify, request
import os
import json
import google.generativeai as genai

app = Flask(__name__)

# Load Dummy Data
def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)

data = load_data()

# Gemini Setup
GEMINI_API_KEY = 'GEMINI_API_KEY'
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')
else:
    print("WARNING: GEMINI_API_KEY not found in environment variables.")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/classes')
def get_classes():
    classes = [{"id": c["id"], "name": c["name"]} for c in data["classes"]]
    return jsonify(classes)

@app.route('/api/subjects/<class_id>')
def get_subjects(class_id):
    for c in data["classes"]:
        if c["id"] == class_id:
            subjects = [{"id": s["id"], "name": s["name"]} for s in c["subjects"]]
            return jsonify(subjects)
    return jsonify({"error": "Class not found"}), 404

@app.route('/api/chapters/<class_id>/<subject_id>')
def get_chapters(class_id, subject_id):
    for c in data["classes"]:
        if c["id"] == class_id:
            for s in c["subjects"]:
                if s["id"] == subject_id:
                    chapters = [{"id": ch["id"], "name": ch["name"]} for ch in s["chapters"]]
                    return jsonify(chapters)
    return jsonify({"error": "Subject not found"}), 404

@app.route('/api/topics/<class_id>/<subject_id>/<chapter_id>')
def get_topics(class_id, subject_id, chapter_id):
    for c in data["classes"]:
        if c["id"] == class_id:
            for s in c["subjects"]:
                if s["id"] == subject_id:
                    for ch in s["chapters"]:
                        if ch["id"] == chapter_id:
                            return jsonify(ch["topics"])
    return jsonify({"error": "Chapter not found"}), 404

@app.route('/api/content/<class_id>/<subject_id>/<chapter_id>/<topic_id>')
def get_content(class_id, subject_id, chapter_id, topic_id):

    
    # Find the topic name
    topic_name = "Unknown Topic"
    for c in data["classes"]:
        if c["id"] == class_id:
            for s in c["subjects"]:
                if s["id"] == subject_id:
                    for ch in s["chapters"]:
                        if ch["id"] == chapter_id:
                            for t in ch["topics"]:
                                if t["id"] == topic_id:
                                    topic_name = t["name"]
                                    break
    
    return jsonify({
        "topic_name": topic_name,
        "explanation": f"Detailed explanation for {topic_name}...",
        "board_qa": [
            {"q": f"What is {topic_name}?", "a": "Standard definition..."}
        ],
        "jee_qa": [
            {"q": f"Advanced problem on {topic_name}", "a": "Solution..."}
        ],
        "notes": f"Key points for {topic_name}..."
    })

@app.route('/api/generate_content', methods=['POST'])
def generate_content():
    if not model:
        return jsonify({"error": "Gemini API key not configured"}), 500
    
    req_data = request.json
    topic_name = req_data.get('topic_name')
    section = req_data.get('section') # 'explanation', 'board_qa', 'jee_qa', 'notes'
    
    prompts = {
        'explanation': f"Explain the topic '{topic_name}' for a CBSE Class 11/12 student. Use extremely simple, easy-to-understand English suitable for students with low proficiency. Use real-life analogies, small examples, and break down complex concepts into very simple steps.",
        'board_qa': f"Provide 20 important Board Exam style questions and answers for the topic '{topic_name}'. IMPORTANT: For every question, put the year/importance tag at the END of the question text, enclosed in double asterisks, e.g., 'What is the unit of force? **[CBSE 2019]**'. Format clearly.",
        'jee_qa': f"Provide 10 important JEE Mains/Advanced level questions with detailed solutions for the topic '{topic_name}'. IMPORTANT: For every question, put the year/importance tag at the END of the question text, enclosed in double asterisks, e.g., 'Calculate the velocity... **[JEE Main 2020]**'. Focus on conceptual depth.",
        'notes': f"Provide concise revision notes and important formulas for the topic '{topic_name}'. Use very simple language and bullet points for easy understanding."
    }
    
    prompt = prompts.get(section, f"Tell me about {topic_name}")
    
    try:
        response = model.generate_content(prompt)
        return jsonify({"content": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ask_ai', methods=['POST'])
def ask_ai():
    print("Received AI request")
    if not model:
        print("Error: Model not configured")
        return jsonify({"error": "Gemini API key not configured"}), 500
    
    req_data = request.json
    query = req_data.get('query')
    context = req_data.get('context', '')
    print(f"Query: {query}")
    
    prompt = f"Context: {context}\nStudent Question: {query}\nProvide a VERY SHORT, CONCISE, and IMPORTANT answer. Focus only on the key points. Avoid long explanations unless absolutely necessary. Keep it brief and to the point."
    
    try:
        response = model.generate_content(prompt)
        print("AI Response generated successfully")
        return jsonify({"answer": response.text})
    except Exception as e:
        print(f"AI Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/quiz/<topic_id>', methods=['POST'])
def generate_quiz(topic_id):
    if not model:
        return jsonify({"error": "Gemini API key not configured"}), 500
    
    # We might want the topic name passed in or look it up, for simplicity let's assume client sends name
    topic_name = request.json.get('topic_name', topic_id)
    
    prompt = f"Generate 5 impactful and conceptual multiple choice questions for the topic '{topic_name}' for CBSE Class 12 level. Return ONLY a JSON array of objects with keys: 'question', 'options' (array of 4 strings), 'correct_answer' (index 0-3), and 'explanation' (string explaining the correct answer)."
    
    try:
        response = model.generate_content(prompt)
        # Clean up markdown if present
        text = response.text.replace('```json', '').replace('```', '').strip()
        quiz_data = json.loads(text)
        return jsonify(quiz_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
from resume_parser import parse_resume
from job_matcher import match_resume_with_job
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return "No file uploaded!"
    file = request.files['file']
    if file.filename == '':
        return "No selected file!"
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    parsed_data = parse_resume(filepath)
    job_score = match_resume_with_job(parsed_data)
    
    return render_template('result.html', name=parsed_data['name'], score=job_score)

if __name__ == '__main__':
    app.run(debug=True)

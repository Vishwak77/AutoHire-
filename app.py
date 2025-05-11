from flask import Flask, render_template, request
import PyPDF2
from utils.resume_matcher import get_similarity

app = Flask(__name__)

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    return ' '.join(page.extract_text() for page in reader.pages if page.extract_text())

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    if request.method == 'POST':
        resume_file = request.files['resume']
        jd_text = request.form['jd']
        if resume_file and jd_text:
            resume_text = extract_text(resume_file)
            score = get_similarity(resume_text, jd_text)
            score = round(score * 100, 2)
    return render_template('index.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)

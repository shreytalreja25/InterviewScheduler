from flask import Flask, request, jsonify
from resume_parser import parse_resume
from ai_model import generate_code

app = Flask(__name__)

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    resume_text = parse_resume(file)
    generated_code = generate_code(resume_text)
    
    return jsonify({"code": generated_code})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, abort
import os

app = Flask(__name__)
DIAGRAM_DIR = "diagrams"

@app.route("/")
def index():
    # List all .mmd files in the diagrams directory
    if not os.path.exists(DIAGRAM_DIR):
        os.makedirs(DIAGRAM_DIR)
    
    diagrams = [f for f in os.listdir(DIAGRAM_DIR) if f.endswith('.mmd')]
    return render_template("index.html", diagrams=diagrams)

@app.route("/view/<filename>")
def view(filename):
    file_path = os.path.join(DIAGRAM_DIR, filename)
    if not os.path.exists(file_path):
        abort(404)
        
    with open(file_path, 'r') as f:
        content = f.read()
        
    return render_template("view.html", diagram_name=filename, content=content)

if __name__ == "__main__":
    os.makedirs(DIAGRAM_DIR, exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port='5012')

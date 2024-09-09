from flask import Flask, request, jsonify, render_template
from scripts.object_detection import process_frame  # Ensure this file exists in the same directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/object_detection')
def object_detection():
    return render_template('object_detection.html')

@app.route('/vehicledetection')
def vehicle_detection():
    return render_template('vehicledetection.html')

@app.route('/textscanning')
def text_scanning():
    return render_template('textscanning.html')

@app.route('/detect_objects', methods=['POST'])
def detect_objects_route():
    data = request.json
    if 'image' not in data:
        return jsonify({"error": "No image data provided"}), 400

    detected_objects = process_frame(data['image'])  # Use the imported function
    return jsonify(detected_objects)

if __name__ == '__main__':
    app.run(debug=True)

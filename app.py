from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "JamaAlca AI Backend is running!"

@app.route('/get_advice', methods=['POST'])
def get_advice():
    data = request.json
    crop = data.get("crop")
    issue = data.get("issue")
    # placeholder AI logic
    return jsonify({
        "crop": crop,
        "issue": issue,
        "advice": f"For {crop} showing {issue}, ensure proper irrigation and pest control."
    })

if __name__ == '__main__':
    app.run(debug=True)
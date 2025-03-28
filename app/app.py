from flask import Flask, jsonify, request, abort

app = Flask(__name__)
API_TOKEN = "mysecrettoken"  # In production, secure this appropriately

def authenticate():
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_TOKEN}":
        abort(401, description="Unauthorized")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200

@app.route('/data', methods=['GET'])
def data():
    authenticate()
    dummy_data = {"id": 1, "message": "This is some dummy data."}
    return jsonify(dummy_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
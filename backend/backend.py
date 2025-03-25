from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS  # Allow frontend to access backend

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from different origins

@app.route("/run", methods=["POST"])
def run_code():
    try:
        code = request.json.get("code", "")

        if not code.strip():
            return jsonify({"output": "⚠️ No code provided!"}), 400

        # Run Python code in a secure subprocess
        process = subprocess.run(
            ["python3", "-c", code],  # Ensure correct Python version
            capture_output=True,
            text=True,
            timeout=5  # Prevent infinite loops
        )

        output = process.stdout if process.stdout else process.stderr
        return jsonify({"output": output})

    except subprocess.TimeoutExpired:
        return jsonify({"output": "⚠️ Code execution timed out!"}), 500

    except Exception as e:
        return jsonify({"output": f"⚠️ Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Use `0.0.0.0` for Render deployment

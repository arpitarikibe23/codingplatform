from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_code():
    try:
        code = request.json.get("code", "")

        if not code:
            return jsonify({"output": "No code provided!"}), 400

        # Run Python code in a subprocess
        process = subprocess.run(
            ["python3", "-c", code],  # Use "python3" for better compatibility
            capture_output=True,
            text=True
        )

        output = process.stdout if process.stdout else process.stderr
        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)  # Make sure it listens on all IPs

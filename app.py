from flask import Flask, request, jsonify, render_template
import subprocess
import shlex
from command_schema import COMMAND_SCHEMA

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/schema")
def schema():
    return jsonify(COMMAND_SCHEMA)


@app.route("/run", methods=["POST"])
def run_command():
    data = request.json
    action = data.get("action")

    if action not in COMMAND_SCHEMA:
        return jsonify({"error": "Invalid command"}), 400

    schema = COMMAND_SCHEMA[action]
    fields = schema["fields"]

    # ✅ Validation
    for key in fields:
        if not data.get(key):
            return jsonify({"error": f"{key} is required"}), 400

    try:
        cmd_raw = schema.get("command_raw", False)
        if schema.get("command_raw", False):
            cmd_list = shlex.split(data["command"])

            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=10
            )

            return jsonify({"output": result.stdout or result.stderr})

        cmd_template = schema["command"]
        final_cmd = []

        for part in cmd_template:
            if part.startswith("{") and part.endswith("}"):
                key = part[1:-1]
                final_cmd.append(str(data.get(key)))
            else:
                final_cmd.append(part)

        result = subprocess.run(
            final_cmd,
            capture_output=True,
            text=True,
            timeout=10
        )

        return jsonify({"output": result.stdout or result.stderr})

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Command timed out"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.run(host="0.0.0.0", port=5000)

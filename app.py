from flask import Flask, render_template, request, redirect
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path("submissions.json")
SCENARIO_FILE = Path("scenario.json")

@app.route("/")
def index():
    with open(SCENARIO_FILE) as f:
        scenario = json.load(f)
    return render_template("index.html", scenario=scenario)

@app.route("/submit", methods=["POST"])
def submit():
    submission = {
        "title":            request.form.get("title", ""),
        "description":      request.form.get("description", ""),
        "objectives":       request.form.get("objectives", ""),
        "roles":            request.form.get("roles", ""),
        "standards":        request.form.get("standards", ""),
        "test_plan":        request.form.get("test_plan", ""),
        "defect_management":request.form.get("defect_management", ""),
        "reviews":          request.form.get("reviews", ""),
        "supplier_control": request.form.get("supplier_control", ""),
        "references":       request.form.get("references", ""),
        "purpose":          request.form.get("purpose", "")
    }

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(submission)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

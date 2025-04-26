# app.py
from flask import Flask, render_template

app = Flask(__name__)

# In-memory storage for demo (reset on server restart)
contact_submissions = []

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/api/contact", methods=["POST"])
def contact_api():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not all([name, email, message]):
            return jsonify({"message": "All fields are required"}), 400

        # Store submission (replace with database in production)
        submission = {
            "name": name,
            "email": email,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        contact_submissions.append(submission)
        print(f"New contact submission: {submission}")  # Log to console

        return jsonify({
            "message": "Message received successfully!",
            "submission": submission
        }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
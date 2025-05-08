import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Jemmy Lim II \n 1st 25 \n ITE 322 \n Semi-Final Exam"
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0' , port=port)

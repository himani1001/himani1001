from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Himani Sharma"
    
    username = os.getenv('USER', os.getenv('USERNAME', 'codepace'))
    
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    top_output = subprocess.getoutput("top -bn1")
    
    response = f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}
    
    TOP output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
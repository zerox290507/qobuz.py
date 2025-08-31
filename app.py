from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.form['link']
    # Run the qobuz-dl CLI script, download to output.flac or similar
    subprocess.run(['python3', 'cli.py', url])
    # Find the downloaded file (edit as needed based on script behavior)
    filename = 'output.flac'  # Change to actual output filename
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    else:
        return "Download Failed", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.form['link']
    # Call your downloader script (save output as song.flac)
    subprocess.run(['python3', 'qobuz_dl.py', url])
    return send_file('song.flac', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
  

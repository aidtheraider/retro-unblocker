from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/fetch" method="post">
            <input type="text" name="url" placeholder="Enter URL">
            <input type="submit" value="Unblock">
        </form>
    '''

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form['url']
    if not url.startswith('http'):
        url = 'http://' + url
    
    try:
        response = requests.get(url)
        return Response(response.content, content_type=response.headers['Content-Type'])
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
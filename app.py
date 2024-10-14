# =[Modules dan Packages]========================

from flask import Flask,render_template,request,jsonify

# =[Variabel Global]=============================

app = Flask(__name__, static_url_path='/static')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]
@app.route("/")
def beranda():
    return render_template('index.html')

# =[Main]========================================
if __name__ == '__main__':

    # Run Flask di localhost
    # app.run(host="localhost", port=5000, debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

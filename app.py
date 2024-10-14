# =[Modules dan Packages]========================
# from flask import Flask,render_template,request,jsonify

from flask import Flask
from flask_ngrok import run_with_ngrok
# =[Variabel Global]=============================

app = Flask(__name__, static_url_path='/static')

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]
@app.route("/")
def beranda():
    return render_template('index.html')

# =[Main]========================================
if __name__ == '__main__':

    # Run Flask di Google Colab menggunakan ngrok
	run_with_ngrok(app)
	app.run()

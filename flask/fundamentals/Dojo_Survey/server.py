from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ["POST"])
def result():
    info_dic = {}
    for k,v in request.form.items():
        if k=="name" and v:
            info_dic["Name: "] =v
        elif k=="Dojo_Location" and v:
            info_dic["Dojo Location: "] =v
        elif k=="Favorite_Language" and v:
            info_dic["Favorite Language: "] =v
        elif k=="Comment" and v:
            info_dic["Comment: "] =v

    return render_template("result.html", contentArr = info_dic)

if __name__=="__main__":
    app.run(debug=True)
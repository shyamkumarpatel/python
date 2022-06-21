from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods = ["POST"])
def process():
    if "user_info" in session:
        session.clear()
    
    session["user_info"] = request.form
        
    return redirect("/result")

@app.route('/result')
def result():
    info_dic = {}
    for k,v in session["user_info"].items():
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
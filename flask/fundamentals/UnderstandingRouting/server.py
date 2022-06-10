from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def sayDojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response

@app.route('/repeat/<times>/<word>')          # The "@" decorator associates this route with the function immediately following
def repeatWord(times,word):
    rtStr = ""
    for i in range(int(times)):
        rtStr += word+'<br>'
    return rtStr  # Return the string 'Hello World!' as a response

@app.route('/<name>')          # The "@" decorator associates this route with the function immediately following
def hello(name):
    return f'Hello {name}!'  # Return the string 'Hello World!' as a response

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

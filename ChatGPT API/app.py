from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "My name is Bao GPT, an artificial mental health therapist"},
        {"role": "user", "content": "I have mental health problem and I need your help"},
        {"role": "assistant", "content": "I am a good adviser and good listener to understand you"},
        {"role": "user", "content": "I want you to be friendly as a friend"}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()


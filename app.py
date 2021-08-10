from flask import Flask, render_template, request, flash, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot.logic.wikipedia_response import WikipediaResponseAdapter
from chatterbot.logic.time_adapter import TimeLogicAdapter
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
#create chatbot
#englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
spanishBot = ChatBot(
	"Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri='sqlite:///database.sqlite3',
	logic_adapters=[
        
        "chatterbot.logic.MathematicalEvaluation",
        #"chatterbot.logic.TimeLogicAdapter",
        
                      {
                          'import_path': 'chatterbot.logic.BestMatch'
                      }
                      #{
                      #    'import_path': 'chatterbot.logic.WikipediaResponseAdapter',
                      #}
        #"chatterbot_weather.WeatherLogicAdapter"
        #"cool_adapter.MyLogicAdapter"
        #{
        #    'import_path': 'chatterbot.voice',
        #    'default_response': 'I am sorry, but I do not understand.'
        #}
    ]
	)
trainer = ChatterBotCorpusTrainer(spanishBot)
trainer.train("chatterbot.corpus.spanish") #train the chatter bot for spanish

#Learn Form

class ReusableForm(Form):
    pregunta = TextField('Pregunta:', validators=[validators.DataRequired()])
    respuesta = TextField('Respuesta:', validators=[validators.DataRequired()])

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(spanishBot.get_response(userText))

@app.route("/", methods=['GET', 'POST'])
def hello():
  form = ReusableForm(request.form)
    
  print(form.errors)
  if request.method == 'POST':
    pregunta=request.form['pregunta']
    respuesta=request.form['respuesta']
  print(pregunta, " ", respuesta)
    
  if form.validate():
  # Save the comment here.
    flash('Gracias por enseñarme ' + pregunta)
  else:
    flash('Error: All the form fields are required. ')
  
  with open('file.json', 'a', encoding ='utf8', newline='\n') as outfile:
    json.dump(request.form, outfile, indent=2)
    outfile.write('\n')


  return render_template('index.html', form=form)
  #return dict(request.form['pregunta'], request.form['respuesta'])


if __name__ == "__main__":
    app.run(debug = True)
  #  app.run()


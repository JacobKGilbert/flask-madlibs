from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hello123'
debug = DebugToolbarExtension(app)

@app.route('/')
def home_route():
  return render_template('home.html', story=story)

@app.route('/story')
def story_route():
  answers = {}
  for arg in request.args:
    answers[arg] = request.args[arg]
  complete_story = story.generate(answers)
  return render_template('story.html', story=complete_story)

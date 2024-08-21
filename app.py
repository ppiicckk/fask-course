from flask import Flask, render_template, jsonify

app = Flask(__name__)

activities = [
  {
    "id" : 1,
    "title" : "body",
    "location" : "Porscarn",
    "condition" : "1m avec temps couvert et vent vent faible side off, marée haute"
  },
  {
    "id" : 2,
    "title" : "city stade",
    "location" : "Combrit",
    "condition" : "soleil"
  },
  {
    "id" : 3,
    "title" : "pump track",
    "location" : "Ploneis",
    "condition" : "temps couvert"
  }
]

@app.route('/')
def home():
  return render_template("home.html", ACTIVITIES = activities)

@app.route('/API/activities')
def lst_activities():
  return jsonify(activities)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

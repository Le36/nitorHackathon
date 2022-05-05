from app import app
from flask import render_template, request, redirect, session
from modules.activites import get_activities

from modules.me import get_me
from modules.users import get_users
from modules.coordinates import get_coordinates
import sys
import nltk, ngrams

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/me", methods=["POST", "GET"])
def me():
    if request.method == "GET":
        return render_template("me.html", me=get_me())


@app.route("/activities", methods=["GET"])
def activities():
    activities = get_activities()
    
    # generated activity
    activityText = "Visit to Reindeer Farm Snowmobile Safari Cross Country Skiing Downhill Skiing"
    activitiesTokenized = [w.lower() for w in nltk.word_tokenize(activityText)]
    lm2 = ngrams.Ngrams(activitiesTokenized)
    lm2.set_weights(0.1, 0.3, 0.2, 0.2, 0.2) 

    words2 = lm2.generate_sentence()
    activityLength = 4
    result = sorted(set(words2[0:activityLength]), key=words2[0:activityLength].index)
    activityCreated =  " ".join(result)
    print(activityCreated, file=sys.stdout)

    # Shakespear opinion
    text = 'shakespeare-hamlet.txt' 
    shakespeareTokenized = [w.lower() for w in nltk.corpus.gutenberg.words(text)]
    lm = ngrams.Ngrams(shakespeareTokenized)
    lm.set_weights(0.01, 0.1, 0.25, 0.15, 0.49)

    start = "Shakespare opinion about this activity: "
    words = lm.generate_sentence(start=nltk.word_tokenize(start))
    shakespearOpinion = " ".join(words)
    print(shakespearOpinion, file=sys.stdout)
    
    return render_template("components/activities.html", activities=activities)

@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == "GET":
        return render_template("components/users.html", data=get_users())


@app.route("/users/<string:user_id>", methods=["POST", "GET"])
def user(user_id):
    if request.method == "GET":
        return render_template(
          "components/user.html", 
          users=get_users(), 
          coordinates=get_coordinates(),
          user_id=user_id
          )

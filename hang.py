import flask
app = flask.Flask("hang")

def get_page(page_name):
    page_html = open(page_name + ".html")
    content = page_html.read()
    page_html.close()
    return content

@app.route("/")
def home():
    return get_page("index")

@app.route("/game")
def game():
    start = flask.request.args.get("start")
    return get_page("game")

@app.route("/guessletter")
def guessletter():
    letter = flask.request.args.get("letter")
    temp_word = ""
    winloss = ""
    secret = ""
    return get_page("game").replace("$$tempword$$", temp_word).replace("$$winloss$$", winloss).replace("$$secret$$", secret)

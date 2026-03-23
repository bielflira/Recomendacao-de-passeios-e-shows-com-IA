from flask import Flask, request, jsonify
import requests
import openai

app = Flask(__name__)
openai.api_key = "SUA_CHAVE_OPENAI"

# eventos
def eventos(musica):
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": "SUA_TICKETMASTER",
        "keyword": musica,
        "countryCode": "BR"
    }

    try:
        data = requests.get(url, params=params).json()
        return [e["name"] for e in data["_embedded"]["events"]]
    except:
        return []

# IA
def ia(locais, musicas):
    prompt = f"Usuário gosta de {locais} e {musicas}. Sugira rolês."
    r = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return r.choices[0].message.content

@app.route("/recomendar", methods=["POST"])
def recomendar():
    data = request.json

    ev = []
    for m in data["musicas"].split(","):
        ev += eventos(m)

    return jsonify({
        "eventos": ev,
        "ia": ia(data["locais"], data["musicas"])
    })

app.run(debug=True)

@app.route("/card/<int:id>")
def card(id):
    card = Card.query.get(id)  # Находим карточку по id
    return render_template("card.html", card=card)

# -*- coding: utf-8 -*-
# author: Magdalena Zubrzycka (magdalenazubrzycka1@gmail.com)

from datetime import datetime
from flask import jsonify, redirect, request, render_template
from models import get_application, Dostawca, Potrawa, Osoba, RODZAJ, Zamowienie

app, db = get_application()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return redirect('/static/img/favicon.ico')


@app.route('/menu.html')
def menu():
    dostawcy = Dostawca.query.all()
    return render_template("szablon_menu.html", dostawcy=dostawcy)


@app.route('/order.html', methods=["POST"])
def order():
    zupa_id = None
    danie_id = None
    for potrawa_id in request.form.getlist("potrawa_id"):
        potrawa = Potrawa.query.filter_by(potrawa_id=potrawa_id).first()
        if potrawa is None:
            continue
        if potrawa.rodzaj == RODZAJ.ZUPA:
            zupa_id = potrawa.potrawa_id
        else:
            danie_id = potrawa.potrawa_id
    zamowienie = Zamowienie(zupa_id=zupa_id, danie_id=danie_id, osoba_id=1, data_dostawy=datetime.today())
    db.session.add(zamowienie)
    db.session.commit()
    return redirect('menu.html')


@app.route('/historia.html')
def historia():
    zamowienia = Zamowienie.query.all()
    return render_template('historia.html', zamowienia=zamowienia)

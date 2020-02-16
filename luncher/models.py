#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Magdalena Zubrzycka (magdalenazubrzycka1@gmail.com)

from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


class RODZAJ:
    ZUPA = 1
    DANIE = 2
    EXTRA = 3


class Osoba(db.Model):
    osoba_id = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(100))
    nazwisko = db.Column(db.String(100))

    def __str__(self):
        return "osoba: {} {}".format(self.imie, self.nazwisko)

    def __repr__(self):
        return self.__str__()


class Dostawca(db.Model):
    dostawca_id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100))
    termin_zamowienia = db.Column(db.DateTime)
    minimalna_liczba = db.Column(db.Integer)
    godzina_dostawy = db.Column(db.Time)

    potrawy = db.relationship('Potrawa', back_populates='dostawca')

    def __str__(self):
        # return "{}: {} \n".format(self.nazwa, ",\n".join (str(potrawa) for potrawa in self.potrawy))
        return "ID: {}, name: {}".format(self.dostawca_id, self.nazwa)

    def __repr__(self):
        return self.__str__()

    def platnosc(self):
        suma_platnosci = 0
        for potrawa in self.potrawy:
            suma_platnosci += potrawa.cena
        return suma_platnosci

    # def cena_dostawy(self, zamowienia):
    #     koszty = get_koszt_by_dostawca(zamowienia)
    #     moje_koszty = koszty.get(self.nazwa, 0)
    #     moje_sztuki = get_liczba_potraw_by_dostawca(zamowienia).get(self.nazwa, 0)
    #     if moje_koszty >= 100 and moje_sztuki >= 5:
    #         cena = 10
    #     elif moje_koszty >= 50 and moje_sztuki >= 3:
    #         cena = 50
    #     elif moje_koszty == 0 and moje_sztuki == 0:
    #         cena = 0
    #     else:
    #         cena = 100
    #     return cena

    def get_zamowione_potrawy(self, zamowienia):
        """
        @type zamowienia: list[Zamowienie]
        @rtype: list[Potrawa]
        """
        return [potrawa for potrawa in Zamowienie.get_lista_potraw(zamowienia) if potrawa.dostawca.nazwa == self.nazwa]
        # zamowione_potrawy = []
        # for potrawa in get_lista_potraw(zamowienia):
        #     if potrawa.dostawca.nazwa == self.nazwa:
        #         zamowione_potrawy.append(potrawa.dostawca.nazwa)
        # return zamowione_potrawy
        # return filter(lambda p: p.dostawcssa.nazwa == self.nazwa, get_lista_potraw(zamowienia))

    def cena_dostawy2(self, zamowienia):
        potrawy = self.get_zamowione_potrawy(zamowienia)
        wartosc_zamowienia = sum([potrawa.cena for potrawa in potrawy])
        # wartosc_zamowienia = 0
        # for potrawa in potrawy:
        #     wartosc_zamowienia += potrawa.cena
        l_zamowien = len(potrawy)


class Potrawa(db.Model):
    potrawa_id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(64))
    rodzaj = db.Column(db.Integer)
    dostawca_id = db.Column(db.Integer, db.ForeignKey('dostawca.dostawca_id'))
    cena = db.Column(db.Integer)

    dostawca = db.relationship("Dostawca", back_populates='potrawy')

    def __str__(self):
        return u"{}, rodzaj: {}, dostawca_id: {}".format(self.nazwa, self.rodzaj, self.dostawca_id)

    def __repr__(self):
        return self.__str__()


class Zamowienie(db.Model):
    zamowienie_id = db.Column(db.Integer, primary_key=True)
    osoba_id = db.Column(db.Integer, db.ForeignKey('osoba.osoba_id'))
    zupa_id = db.Column(db.Integer, db.ForeignKey('potrawa.potrawa_id'))
    danie_id = db.Column(db.Integer, db.ForeignKey('potrawa.potrawa_id'))
    data_dostawy = db.Column(db.DateTime)
    godzina_zamowienia = db.Column(db.Time)
    priorytet = db.Column(db.Integer)
    zrealizowane = db.Column(db.Boolean)

    zupa = db.relationship("Potrawa", foreign_keys=[zupa_id])
    danie = db.relationship("Potrawa", foreign_keys=[danie_id])
    osoba = db.relationship("Osoba")

    @staticmethod
    def sprawdz_zamowienie(zupa, danie):
        if zupa is None and danie is None:
            return u"Nic nie wybrano"
        if zupa is not None and zupa.rodzaj != RODZAJ.ZUPA:
            return u"Błąd wyboru. Zupa jest daniem."
        if danie is not None and danie.rodzaj == RODZAJ.ZUPA:
            return u"Błąd wyboru. Danie to zupa"
        if zupa is not None and danie is not None and danie.rodzaj == RODZAJ.EXTRA:
            return u" Nie można zamówić dania extra wrz z zupą."
        return None

    def cena(self):
        """
        @rtype: int
        """
        if self.zupa is not None and self.danie is not None:
            return self.zupa.cena + self.danie.cena
        elif self.zupa is not None:
            return self.zupa.cena
        elif self.danie is not None:
            return self.danie.cena
        return 0

    @staticmethod
    def get_lista_potraw(zamowienia):
        """
        @type zamowienia: list[Zamowienie]
        @rtype: list[Potrawa]
        """
        lista_potraw = []
        for zamowienie in zamowienia:
            if not zamowienie.zrealizowane:
                continue
            if zamowienie.zupa is not None:
                lista_potraw.append(zamowienie.zupa)
            if zamowienie.danie is not None:
                lista_potraw.append(zamowienie.danie)
        return lista_potraw

        # def cena(self):
        #     if self.zupa is None:
        #         return self.danie.cena
        #     elif self.danie is None:
        #         return self.zupa.cena
        #     return self.zupa.cena + self.danie.cena


db.create_all()


def get_application():
    return app, db

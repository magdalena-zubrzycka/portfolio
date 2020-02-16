# -*- coding: utf-8 -*-
# author: Magdalena Zubrzycka (magdalenazubrzycka1@gmail.com)
from datetime import datetime

from luncher.models import get_application, Osoba, Zamowienie, Potrawa, Dostawca, RODZAJ


app, db = get_application()


d = Dostawca(nazwa="Do syta", minimalna_liczba=3)
db.session.add(d)
db.session.commit()
db.session.add(Potrawa(nazwa="Szczawiowa", rodzaj=RODZAJ.ZUPA, dostawca_id=d.dostawca_id, cena=6))
db.session.add(Potrawa(nazwa="Jarzynowa", rodzaj=RODZAJ.ZUPA, dostawca_id=d.dostawca_id, cena=6))
db.session.add(Potrawa(nazwa="Koperkowa", rodzaj=RODZAJ.ZUPA, dostawca_id=d.dostawca_id, cena=6))
db.session.add(Potrawa(
    nazwa=u"Kurczak tika masala + ryż + surówka z czerwonej kapusty", rodzaj=RODZAJ.DANIE,
    dostawca_id=d.dostawca_id, cena=12))
db.session.add(Potrawa(
    nazwa=u"Roladki wieprzowe z pieczarkami + ziemniaki puree + surówka z kapusty kiszonej", rodzaj=RODZAJ.DANIE,
    dostawca_id=d.dostawca_id, cena=12))
db.session.add(Potrawa(
    nazwa=u"Makaron chiński z warzywami + surówka z czerwonej kapusty (vege)", rodzaj=RODZAJ.DANIE,
    dostawca_id=d.dostawca_id, cena=12))
db.session.add(Potrawa(
    nazwa=u"Dorsz w chrupiącej panierce + ziemniaki opiekane + surówka z kapusty kiszonej", rodzaj=RODZAJ.EXTRA,
    dostawca_id=d.dostawca_id, cena=18))
db.session.commit()


d = Dostawca(nazwa="Pobudka", minimalna_liczba=1)
db.session.add(d)
db.session.commit()
db.session.add(Potrawa(
    nazwa=u"Filet z łososia z makaronem i rukolą", rodzaj=RODZAJ.EXTRA, dostawca_id=d.dostawca_id, cena=18))
db.session.add(Potrawa(
    nazwa=u"Morszczuk w panierce, ziemniaki opiekane, surówka ", rodzaj=RODZAJ.EXTRA, dostawca_id=d.dostawca_id,
    cena=18))
db.session.add(Potrawa(
    nazwa=u"Pierogi z mięsem", rodzaj=RODZAJ.DANIE, dostawca_id=d.dostawca_id, cena=18))
db.session.add(Potrawa(
    nazwa=u"VEGE makaron arabiatta", rodzaj=RODZAJ.DANIE, dostawca_id=d.dostawca_id, cena=18))
db.session.commit()


db.session.add(Osoba(imie="Jan", nazwisko="Kowalski"))
db.session.add(Osoba(imie="Robert", nazwisko=u"Iksiński"))
db.session.commit()


exit(0)

p = Potrawa(nazwa="kotlet", rodzaj=RODZAJ.DANIE, dostawca_id=d.dostawca_id, cena=10)
p1 = Potrawa(nazwa="szczawiowa", rodzaj=RODZAJ.ZUPA, dostawca_id=d.dostawca_id, cena=6)
p2 = Potrawa(nazwa="golonka", rodzaj=RODZAJ.EXTRA, dostawca_id=d.dostawca_id, cena=20)
db.session.add(p)
db.session.add(p1)
db.session.add(p2)
db.session.commit()
z1 = Zamowienie(osoba_id=o.osoba_id, danie_id=p.potrawa_id)
z2 = Zamowienie(osoba_id=o2.osoba_id, zupa_id=p1.potrawa_id)
db.session.add(z1)
db.session.add(z2)


db.session.commit()

potrawy = Potrawa.query.all()
print ("Potrawy {}".format(potrawy))

potrawa_by_id = {potrawa.potrawa_id: potrawa for potrawa in potrawy}
dostawcy = Dostawca.query.all()
dostawca_by_id = {dostawca.dostawca_id: dostawca for dostawca in dostawcy}

for potrawa in potrawy:
    print("Dict: Potrawa: {}, Dostawca {}".format(potrawa, dostawca_by_id[potrawa.dostawca_id]))

for potrawa in potrawy:
    print("Relacja: Potrawa: {}, Dostawca {}".format(potrawa, potrawa.dostawca))

zamowienia = Zamowienie.query.all()
zamowienie_by_id = {zamowienie.zamowienie_id : zamowienie for zamowienie in zamowienia}
osoby = Osoba.query.all()
osoba_by_id = {osoba.osoba_id: osoba for osoba in osoby}

for zamowienie in zamowienia:
    print("id zamowienia {} : {}".format(zamowienie.zamowienie_id, osoba_by_id[zamowienie.osoba_id].imie))

print d.potrawy
potrawy = Potrawa.query.order_by(Potrawa.cena.asc()).all()
# order_by kolejnoc wyników(po czym ma być kolejność)
# desc - MALEJĄCO
# asc - rosnąco
print ("NIektore potrawy {}".format(potrawy))


## inny przykład z bazą danych:


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author')
    posts = db.relationship('Post', back_populates='author')

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User", back_populates='posts')

    def __repr__(self):
        return '<Post {1} {0}>'.format(self.body, self.id)


u = User(username='Magda', email='magda@example.com')
db.session.add(u)
u = User(username='Alunia', email='alunia@example.com')
db.session.add(u)
u_agnieszka = User(username='Agnieszka', email='agnieszka@example.com')
db.session.add(u_agnieszka)

# print "dodani uzytkonicy przed commit", User.query.all()
db.session.commit()

users = User.query.all()
print "dodani uzytkonicy po commit", users

p = Post(body='my first post!', author=u_agnieszka)
db.session.add(p)
db.session.commit()
# print User.query.order_by(User.username.desc()).all()
# print u.posts
p = Post.query.all()[0]
print p

p = Post(body='my next post!', author=u)
db.session.add(p)
db.session.commit()
# print User.query.order_by(User.username.desc()).all()
# print u.posts
user_by_ids = {u.id: u for u in users}

posty = Post.query.all()
post_by_ids = {p.id: p for p in posty}
print posty
for elem in posty:
    print("{} {}".format(elem, user_by_ids[elem.user_id]))

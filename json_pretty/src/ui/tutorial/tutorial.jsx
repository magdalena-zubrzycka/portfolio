// @flow
import React from 'react';

function powitaj(imie) {
    const a = '';
    return <span> super {imie} </span>;
}
const powitaj1 = function (imie) {
    const a = '';
    return <span> super {imie} </span>;
};
const powitaj2 = (imie) => {
    const a = '';
    return <span> super {imie} </span>;
};
const powitaj3 = imie => (
    <span> super witam {imie} </span>
);
const Powitanie = ({ imie, nazwisko }) => (
    <span> super react {imie} <i>{nazwisko}</i></span>
);

const imie = 'Magda';

const te1 = powitaj(imie);
const te2 = powitaj2('Agnieszka');
const te3 = powitaj3('Ala');
const imiona = ['Agnieszka', 'Alicja'];
const body = [];
for (let i = 0; i < imiona.length; i++) {
    body.push(<h3>{powitaj3(imiona[i])}</h3>);
}

const slowanik = {jeden: 11, dwa: 22, trzy: 33};
const { jeden, dwa, cztery } = slowanik;
const trzy = 33;
const slowanik2 = { jeden, dwa, trzy };
const tablica2 = [jeden, dwa, trzy];

const body2 = imiona.map((imie) => (<h3>{ powitaj3(imie) }</h3>));

const body3 = imiona.map(
  (im) => (<h3><Powitanie imie={im} nazwisko="Kowalska" /></h3>));


const header = <h1>{ [ "hello, word!", te1, te2, <span>{jeden} {dwa} {cztery}</span>] } </h1>;

const miasta = ['londyn', 'warszawa', 'barcelona'];
const linki = miasta.map(
    miasto => ([
        <a href={ `szczeguly/${ miasto }.html` }>{miasto}</a>,
        <img src={`static/img/${ miasto }.png`} />,
        <br/>
    ])
);
const Miasto = ({miasto}) => (
    <div>
        <a href={ `szczeguly/${ miasto }.html` }>{miasto}</a>
        <img src={`static/img/${ miasto }.png`} />
    </div>
);
const linki2 = miasta.map(
  (misto) => <Miasto miasto={misto} />
)

const Tutorial = ({ }) => (
    <div>{[header, [body, body2, body3], linki]}</div>
);

export default Tutorial;

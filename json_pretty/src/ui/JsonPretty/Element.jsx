// @flow
import React from 'react';
import Tablica from './Tablica';
import Slownik from './Slownik';


function isDict(v) {
    return typeof v === 'object' && v !== null && !(v instanceof Array) && !(v instanceof Date);
}

function isArray(v) {
    return v !== null && v instanceof Array;
}
function isString(v) {
    return typeof v === 'string' || v instanceof String;
}
function isNumber(v) {
    return v !== null && !isString(v) && !isNaN(v);
}


const Element = ({ wartosc, zaglebienie }) => {
    if (wartosc === null) {
        return <span>null</span>;
    }
    if (isDict(wartosc)) {
        return <Slownik slownikDoWypisania={wartosc} zaglebienie={zaglebienie} />;
    }
    if (isArray(wartosc)) {
        return <Tablica tablicaDoWypisania={wartosc} zaglebienie={zaglebienie} />;
    }
    if (isString(wartosc)) {
        return <span> {JSON.stringify(wartosc)} </span>;
    }
    if (isNumber(wartosc)) {
        return <span>{wartosc}</span>;
    }
    return 'dupa';
};
export default Element;

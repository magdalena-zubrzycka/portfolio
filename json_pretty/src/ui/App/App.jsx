// @flow
import React from 'react';
import { shouldUpdate } from 'recompose';
import "bootstrap/scss/bootstrap.scss"
import _ from 'lodash';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import JsonPretty from '/ui/JsonPretty';
import style from './App.scss';


const App = () => (
    <div className={style.page}><JsonPretty/></div>
);

export default App;

// @flow
import React from 'react';
import { shouldUpdate } from 'recompose';
import _ from 'lodash';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import JsonPretty from '/ui/JsonPretty';


const App = () => (
    <div><JsonPretty/></div>
);

export default App;

// @flow
import React from 'react';
import Element from './Element';


const przykladowy = {
    jeden: 1,
    dwa: '2',
    tablica: [
        3,
        4,
        null,
        {
            najd: 5,
            kjie: 4
        },
        'coś',
    ],
    nic: null
};


class JsonPretty extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: '{"jeden": 1,"dwa": "2","tablica": [3,4,  null,{  "nakkkjd": 5,  "kjie": 4  },  "coś"  ],  "nic": null}',
            wartosc: {}
        };
    }
    render() {
        return (
            <div>
                <h1>JSON Pretty</h1>
                <textarea value={this.state.text} onChange={event => this.setState({ text: event.target.value })} />
                <div>
                    <button onClick={() => this.setState({ wartosc: JSON.parse(this.state.text) })}>Przetwórz</button>
                </div>
                <div><Element wartosc={this.state.wartosc} zaglebienie={1} /></div>
            </div>
        );
    }
}

export default JsonPretty;

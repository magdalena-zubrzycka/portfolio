// @flow
import React from 'react';
import Element from './Element';


class Tablica extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            zwiniety: props.zaglebienie > 2,
        };
    }

    render() {
        const { tablicaDoWypisania, zaglebienie } = this.props;
        const { zwiniety } = this.state;
        if (zwiniety) {
            return (
                <span>
                [
                    <button onClick={() => this.setState({ zwiniety: false })}>
                     +
                    </button>
                ]
                </span>
            );
        }
        const wiersze = [];
        for (let i = 0; i < tablicaDoWypisania.length; i += 1) {
            wiersze.push(
                <span>
                    {'\u00A0'.repeat(zaglebienie * 4)}
                    <Element wartosc={tablicaDoWypisania[i]} zaglebienie={zaglebienie + 1} />
                    {i + 1 === tablicaDoWypisania.length ? '' : ','}
                    <br />
                </span>);
        }
        return (
            <span>
             [
                <button onClick={() => this.setState({ zwiniety: true })}>
                   -
                </button>
                <br />{wiersze}
                {'\u00A0'.repeat(zaglebienie * 4 - 4)}
             ]
            </span>
        );
    }
}

export default Tablica;

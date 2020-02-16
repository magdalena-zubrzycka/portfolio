// @flow
import React from 'react';
import Element from './Element';


class Slownik extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            zwiniety: props.zaglebienie > 2,
        };
    }

    render() {
        const { slownikDoWypisania, zaglebienie } = this.props;
        const { zwiniety } = this.state;
        if (zwiniety) {
            return (
                <span>
                    {'{'}
                    <button onClick={() => this.setState({ zwiniety: false })}>
                        +
                    </button>
                    {'}'}
                </span>);
        }
        const wiersze = [];
        const entries = Object.entries(slownikDoWypisania);
        for (let i = 0; i < entries.length; i += 1) {
            wiersze.push(
                <span>
                    {'\u00A0'.repeat(zaglebienie * 4)}
                    {JSON.stringify(entries[i][0])}:
                    <Element wartosc={entries[i][1]} zaglebienie={zaglebienie + 1} />
                    {i + 1 === entries.length ? '' : ','}
                    <br />
                </span>);
        }
        return (
            <span>
                {'{'}
                <button onClick={() => this.setState({ zwiniety: true })}>
                    -
                </button>
                <br />{wiersze}
                {'\u00A0'.repeat(zaglebienie * 4 - 4)}
                {'}'}
            </span>
        );
    }
}

export default Slownik;

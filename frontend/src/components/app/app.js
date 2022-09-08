import React, { Component } from 'react';
import CardService from '../../services/card-service';

export default class App extends Component {

  state = {
    cardService: new CardService(),
  };

  render() {
    this.state.cardService.getAllPersons().then(result => {
          result.map(item => console.log(item))
          result.map(item => this.state.cardService.getCard(item.id).then(resultCard => console.log(resultCard)))
        }
    )
    return (
        <div>Test</div>
    )
  }
}

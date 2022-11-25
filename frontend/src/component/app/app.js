import React, { Component } from 'react';
import CardService from '../../service/card-service';
import card from '../../page/card'
import signup from '../../page/signup'
import login from '../../page/login';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import { ThemeProvider as MuiThemeProvider } from '@material-ui/core/styles';


export default class App extends Component {

  state = {
    cardService: new CardService(),
  };

  render() {

    return (
      <MuiThemeProvider>
      <BrowserRouter>
        <div>
          <Switch>
            <Route exact path="/login" component={login} />
            <Route exact path="/signup" component={signup}/>
            <Route exact path="/" component={card}/>
          </Switch>
        </div>
      </BrowserRouter>
      </MuiThemeProvider>
    );
  }
}

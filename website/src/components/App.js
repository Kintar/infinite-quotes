import React, { Component } from 'react';
import QuotesAppBar from './QuotesAppBar';
import Button from 'material-ui/Button'

import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles/';

import { green, deepOrange, red } from 'material-ui/colors/'

import AddIcon from 'material-ui-icons/Add'

import './App.css';
import './flexboxgrid.min.css'

import AddQuote from './AddQuote'
import quotesTheme from './quotesTheme'

class App extends Component {
  render() {
    return (
    	<MuiThemeProvider theme={quotesTheme}>
			<QuotesAppBar />
			<AddQuote />
		</MuiThemeProvider>
    );
  }
}

export default App;

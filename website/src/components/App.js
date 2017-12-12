import React, { Component } from 'react';
import QuotesAppBar from './QuotesAppBar';
import QuotesPanel from './QuotesPanel';

import { MuiThemeProvider } from 'material-ui/styles/';

import './App.css';
import './flexboxgrid.min.css'

import AddQuote from './AddQuote'
import quotesTheme from './quotesTheme'

class App extends Component {
  render() {
    return (
    	<MuiThemeProvider theme={quotesTheme}>
			<QuotesAppBar />
			<QuotesPanel />
			<AddQuote />
		</MuiThemeProvider>
    );
  }
}

export default App;

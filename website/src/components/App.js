import React, { Component } from 'react';
import QuotesAppBar from './QuotesAppBar';
import QuotesPanel from './QuotesPanel';
import Dialog, {DialogTitle, DialogActions, DialogContent} from 'material-ui/Dialog';
import Button from 'material-ui/Button';
import Typography from 'material-ui/Typography';

import { MuiThemeProvider } from 'material-ui/styles/';

import './App.css';
import AddQuote from './AddQuote';

import quotesTheme from './quotesTheme';

class App extends Component {
	state = {
		alertOpen: false,
		authorized: false
	};

	openAlertDialog = () => {
		this.setState({alertOpen: true});
	}

	handleDialogClose = () => {
		this.setState({alertOpen: false});
	}

	render() {
		const { auth } = this.state;

		return (
			<MuiThemeProvider theme={quotesTheme}>
				<QuotesAppBar auth={this.state.auth} />
				<QuotesPanel />
				{auth && (
				<AddQuote onClick={this.openAlertDialog} />
				)}
				<Dialog open={this.state.alertOpen}>
					<DialogTitle>Coming Soon!</DialogTitle>
					<DialogContent>
						<Typography type="body1">We're not ready to accept new quotes just yet.  Check back soon!</Typography>
					</DialogContent>
					<DialogActions>
						<Button onClick={this.handleDialogClose} color="primary">Ok</Button>
					</DialogActions>
				</Dialog>
			</MuiThemeProvider>
		);
	}
}

export default App;

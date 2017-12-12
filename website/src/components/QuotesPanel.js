import React, { Component } from 'react';
import Grid from 'material-ui/Grid';
import quotesClient from './quotesClient';
import QuoteCard from './QuoteCard';

class QuotesPanel extends Component {
	constructor(props) {
		super(props);
		this.state = { startKey: '', group: 'testing', quotes: [] };
		this.client = quotesClient;
	}

	componentWillUnmount() {

	}

	componentDidMount() {
		this.getNextQuotePage();
	}

	getNextQuotePage() {
		var args = {
			path: { group: this.state.group },
			args: { startKey : this.state.startKey }
		};

		
		var req = this.client.methods.getPage(args, (data, response) => {
			data.items.concat(this.state.quotes);
			this.setState({ quotes: data.items });
		});

		req.on('requestTimeout', function(req) {
			alert("Quote page request timed out");
			req.abort();
		});

		req.on('responseTimeout', function(req) {
			alert("Quote page response timed out");
			req.abort();
		})

		req.on('error', function() { alert("Error loading quotes"); });
	}

	render() {
		return(
			<Grid container >
				{this.state.quotes.map(quote => (
					<QuoteCard quote={quote} key={quote.timestamp} />
				))}
			</Grid>
		);
	}
}

export default QuotesPanel;
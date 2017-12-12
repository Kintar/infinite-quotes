import React, { Component } from 'react';
import {GridList, GridListTile } from 'material-ui/GridList';

import quotesClient from './quotesClient';

const styles = theme => ({
	root: {
		display: 'flex',
		flexWrap: 'wrap',
		justifyContent: 'space-around',
		overflow: 'hidden',
		background: theme.palette.background.paper
	},
	gridList: {
		width: 500
	}
})

class QuotesPanel extends Component {
	constructor(props) {
		super(props);
		this.classes = props;
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

		
		var req = quotesClient.methods.getPage(args, (data, response) => {
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
			<div className={this.classes.root}>
				<GridList cellHeight={160} className={this.classes.gridList} cols={6}>
					{this.state.quotes.map(quote => (
						<GridListTile key={quote.timestamp} cols={1}>
							{quote.lines.map(line => (
								<p>{line.text}</p>
							))}
						</GridListTile>
					))}
				</GridList>
			</div>
		);
	}
}

export default QuotesPanel;
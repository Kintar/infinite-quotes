import React, { Component } from 'react';
import Grid from 'material-ui/Grid';
import Card from 'material-ui/Card';
import Typography from 'material-ui/Typography';
import Divider from 'material-ui/Divider';
import { withStyles } from 'material-ui/styles';

const style = {
	root: {
		padding: '8px 8px 4px 8px',
		margin: 0
	}
}

class QuoteCard extends Component {
	render() {
		var quote = this.props.quote;
		return (
			<Grid item xs={12} sm={6} md={3} lg={2} xl={2}>
				<Card>
					<Grid container spacing={8} >
						{quote.lines.map((line, index) => (
							<React.Fragment key={quote.timestamp + ":" + index}>
								<Grid item xs={2}>
									<Typography align="right" type="body1">{line.quoter}:</Typography>
								</Grid>
								<Grid item xs={10}>
									<Typography type="body1">"{line.text}"</Typography>
								</Grid>
							</React.Fragment>
						))}
						<Grid item xs={12}>
							<Divider />
							<Typography className={this.props.classes.root} align="right" type="caption">{new Date(quote.timestamp * 1000).toISOString().split('T')[0]}</Typography>
						</Grid>
					</Grid>
				</Card>
			</Grid>
		);
	}
}

export default withStyles(style)(QuoteCard);
import React, { Component } from 'react';
import { withStyles } from 'material-ui/styles'

import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';

const styles = {
	root: {
		width: '100%',
	},
	flex: {
		flex: 1,
	},
	menuButton: {
		marginLeft: -12,
		marginRight: 20
	}
}

class QuotesAppBar extends Component {
	render() {
		const { classes } = this.props;
		return (
			<div className={classes.root}>
				<AppBar position="static">
					<Toolbar>
						<Typography type="title" color="inherit">
							Infinite Quotes
						</Typography>
					</Toolbar>
				</AppBar>
			</div>
		);
	}
}

export default withStyles(styles)(QuotesAppBar);
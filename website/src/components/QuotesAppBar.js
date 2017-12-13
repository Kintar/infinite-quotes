import React, { Component } from 'react';
import { withStyles } from 'material-ui/styles';
import Button from 'material-ui/Button';
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
}

class QuotesAppBar extends Component {
	render() {
		const { classes, auth } = this.props;
		return (
			<div className={classes.root}>
				<AppBar position="static">
					<Toolbar>
						<Typography type="title" color="inherit" className={classes.flex}>
							Infinite Quotes
						</Typography>
						{!auth && (
							<Button color="contrast">
								Login
							</Button>
						)}
					</Toolbar>
				</AppBar>
			</div>
		);
	}
}

export default withStyles(styles)(QuotesAppBar);
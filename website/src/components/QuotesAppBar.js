import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles'

import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import Button from 'material-ui/Button';
import IconButton from 'material-ui/IconButton';
import MenuIcon from 'material-ui-icons/Menu';

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
						<IconButton className={classes.menuButton} color="contrast" aria-label="Menu">
							<MenuIcon />
						</IconButton>
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
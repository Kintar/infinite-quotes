import React, { Component } from 'react';
import Button from 'material-ui/Button'
import AddIcon from 'material-ui-icons/Add'
import { withStyles } from 'material-ui/styles'

const styles = theme => ({
	addButton: {
		position: 'absolute',
		right: 0,
		bottom: 0,
		margin: theme.spacing.unit * 2
	}
});

class AddQuote extends Component {
  render() {
  	const { classes } = this.props;
    return (
			<Button fab color="accent" className={classes.addButton} >
				<AddIcon />
			</Button>
    );
  }
}

export default withStyles(styles)(AddQuote);
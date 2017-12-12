import React, { Component } from 'react';
import Grid from 'material-ui/Grid';
import Card from 'material-ui/Card';
import Typography from 'material-ui/Typography';
import Divider from 'material-ui/Divider';
import { withStyles } from 'material-ui/styles';
import Dialog, {DialogTitle} from 'material-ui/Dialog';

const styles = {

}

class AlertDialog extends Component {
	state = {
		open: false
	};

	handleOpen = () => {
		this.setState({open : true});
	}

	render() {
		return (
			<Dialog open={this.state.open}>
				<DialogTitle>{this.props.title}</DialogTitle>
				<Typography type="body1">{this.props.message}</Typography>
			</Dialog>
		);
	}
}

export default withStyles(styles)(AlertDialog);
import {green, deepOrange} from 'material-ui/colors/'
import createMuiTheme from 'material-ui/styles/createMuiTheme';

var quotesTheme = createMuiTheme({
  palette: {
    primary: green,
    secondary: deepOrange,
    text: {
      contrast: "rgba(1,1,1,0.87)"
    }
  }
});

export default quotesTheme;
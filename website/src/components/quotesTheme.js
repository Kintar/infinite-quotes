import createMuiTheme from 'material-ui/styles/createMuiTheme';

const iqpalette = {
    50: '#e7e4ee',
    100: '#c2bbd6',
    200: '#9a8eba',
    300: '#72609e',
    400: '#533e8a',
    500: '#351c75',
    600: '#30196d',
    700: '#281462',
    800: '#221158',
    900: '#160945',
    A100: '#917cff',
    A200: '#6649ff',
    A400: '#3b16ff',
    A700: '#2800fc',
    'contrastDefaultColor': 'light',
};

const quotesTheme = createMuiTheme({
  palette: {
    'type': 'dark',
    primary: iqpalette,
    secondary: iqpalette
  }
});

export default quotesTheme;
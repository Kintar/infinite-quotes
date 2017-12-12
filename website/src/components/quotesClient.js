var Client = require('node-rest-client').Client;

const quotesClient = new Client();

quotesClient.registerMethod('getPage', 'https://py8n4ohrj5.execute-api.us-east-2.amazonaws.com/Prod/quotes/${group}', 'GET');

export default quotesClient;
import {Config, CognitoIdentityCredentials} from "aws-sdk";
import {
	AuthenticationDetails,
	AuthenticationHelper,
	CognitoAccessToken,
	CognitoIdToken,
	CognitoRefreshToken,
	CognitoUser,
	CognitoUserAttribute,
	CognitoUserPool,
	CognitoUserSession,
	CookieStorage,
	DateHelper
} from 'amazon-cognito-identity-js';

const CognitoConfig = {
	region: 'us-east-2',
	identityPoolId: 'us-east-2_KX8gUwVEr',
	clientId: '5pkt66jto68tseds317puj9i15'
};

Config.region = 'us-east-2';
Config.credentials = new CognitoIdentityCredentials({
	IdentityPoolId: CognitoConfig.identityPoolId
});

const UserPool = new CognitoUserPool({
	UserPoolId: CognitoConfig.identityPoolId,
	ClientId: CognitoConfig.clientId
})

export default CognitoConfig;
export default UserPool;
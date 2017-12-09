# DocPad Configuration File
# http://docpad.org/docs/config

# Define the DocPad Configuration
docpadConfig = {
	templateData:
		site:
			url: "http://quotes.infinities-within.net"
			title: "Infinite Quotes"
			description: """
				A location for our merry band of misfits to share interesting, amusing, or downright
				weird quotes.  Also the reference implementation for the Infinite Quotes quotewall
				system. <a href="http://github.com/Kintar/infinite-quotes">(GitHub Link)</a>
				"""
			keywords: """
				quotes comedy aws
				"""

		# Helper functions for stupidity of CSS and MDL
		buttonCss: ->
			'mdl-button mdl-js-button mdl-button--raised mdl-button--colored mdl-js-ripple-effect'
}

# Export the DocPad Configuration
module.exports = docpadConfig
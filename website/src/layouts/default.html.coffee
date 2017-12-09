doctype 5
html ->
	head ->
		title "#{@site.title} | #{@document.title}"
		text @getBlock('meta').toHTML()
		text @getBlock('styles').toHTML()
		text @partial 'main-style'
	body ->
		text @content
		text @getBlock('scripts').toHTML()
		text @partial 'footer'
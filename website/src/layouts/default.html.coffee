doctype 5
html ->
	head ->
		meta charset: 'utf-8'
		title "#{@site.title} | Home"
		meta(name: 'description', content: @desc) if @desc?
		@partial 'main-style'
	body ->
		h1 @document.title
		@content
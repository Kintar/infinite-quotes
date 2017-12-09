doctype 5
html ->
	head ->
		title #{@site.title}
		text @getBlock('meta').toHTML()
		text @getBlock('styles').toHTML()
		text @partial 'main-style'
	body ->
		div class: 'mdl-layout mdl-js-layout', ->
			header class: 'mdl-layout__header', ->
				div class: 'mdl-layout-icon', ->

				div class: 'mdl-layout__header-row', ->
					span class: 'mdl-layout__title', ->
						@site.title
					div class: 'mdl-layout-spacer', ->
					nav class: 'mdl-navigation', ->
						a class: 'mdl-navigation__link', href: '#', 'About'
						a class: 'mdl-navigation__link', href: '#', 'Sign In'

			div class: 'mdl-layout__drawer', ->
				span class: 'mdl-layout__title', ->
					@site.title
				nav class: 'mdl-nagivation':
					a class: 'mdl-navigation__link', href: '#', 'Group'

			main class: 'mdl-layout__content', ->
				text @content
			
			text @getBlock('scripts').toHTML()
			text @partial 'footer'
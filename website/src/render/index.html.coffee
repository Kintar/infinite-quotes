---
title: "Home"
layout: "default"
isPage: true
---

div class: 'quote-card-container', ->
	div class: 'mdl-card mdl-shadow--2dp', ->
		div class: 'mdl-card__supporting-text', ->
			div class: 'quoter-text', ->
				'AL'
			div class: 'quote-text', ->
				text '"Well,'
				em 'THAT'
				text 'happened..."'
			div class: 'quoter-text', ->
				'JC'
			div class: 'quote-text', ->
				text '"You can\'t prove it."'
			div class: 'mdl-card__actions', ->
				button class: @buttonCss(), style: 'float: right', 'Edit'

	button class: 'mdl-button mdl-js-button mdl-button--fab mdl-button--colored add-button', ->
		i class: 'material-icons', 'add'
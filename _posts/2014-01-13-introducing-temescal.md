---
layout: post
title: Introducing Temescal
published: true
category: 
tags: []
---
Hey look! Another year another blog post from me. Maybe 2014 will yield more than three of them.

This post is a little different/special in that, instead of quipping about tech news or sharing my opinions, I'm announcing what I feel is my first significant contribution back to the developer community - [Temescal](https://github.com/todd/temescal).

Temescal, named after the the district in Oakland, is Rack middleware for JSON APIs that catches exceptions and renders them as nicely formatted JSON. It adds greater consistency, even in the face of failure, to APIs without you having to write any of your own error handling logic.

Temescal will even play nice with monitoring services and report the errors it catches to them, assuming they're configured, of course. Only two services (Airbrake and New Relic) are supported at the moment, but I'll gladly add support for other services that there's a demand for (or, better yet, send a pull request!).

The first beta release of Temescal is available via [RubyGems](http://rubygems.org/gems/temescal) and the source is on [GitHub](https://github.com/todd/temescal). I encourage you to check out the gem and the source and let me know what you think!
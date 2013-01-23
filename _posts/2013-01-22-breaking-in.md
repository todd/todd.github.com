---
layout: post
title: Breaking In
published: true
category:
tags: []
---
_Probably a year or so ago, I was standing in the computer section of a bookstore. A kid, probably 14 or 15, struck up a conversation with me and asked me what I knew about making games for the iPhone. I exhausted my limited knowledge of the topic with him - that he'd need to learn Objective-C and a rendering engine of some sort. I asked him what kind of programming experience he had - none at all, he told me. As gently as I could, I had to tell him that what he wanted to do was not something a beginner could tackle by themselves. I picked an introduction to Objective-C book off the shelf, handed it to him, and told him that it should get him started on basic iOS development and that, once he understood the basics, he could probably start to learn how to make games on iOS. He took the book, thanked me, and wandered off. As I was leaving, I found the book lying on a shelf in an adjacent aisle._

Fair warning - I'm going to pick on Rails a bit in this post since that's what I have the most exposure to these days and it's what I'm most frequently asked about. That's not to say that Rails isn't a great framework (it is) - I'm simply exploring the culture of Rails (and really, all complex frameworks out there) and beginners.

One of the questions I frequently get asked by non- or semi-technical friends and acquaintances is how they can go about teaching themselves Rails/Django/Node/insert-framework-here. All too often, I have to explain why this is the wrong question.

If you have limited-to-no programming experience, you shouldn't start by trying to teach yourself these frameworks. Instead, a beginner should be asking "what fundamentals do I need to understand to use a complex framework like Rails?" When I say fundamentals, I mean basic things like data structures, data flow, OOP, basic recursion - essentially all the things that a first-year computer science student would learn. I also think that learning SQL is important - even if you're using an ORM to query data for you, it's still important to understand what it's doing. If you don't understand any of what I just wrote, stop your Rails tutorial and go read a book or take a night class at a JC so you can pick up these concepts. All too often, I'll have a friend show me the Twitter clone they built as part of their Rails tutorial but not really understand why they wrote what they wrote. If you are an absolute beginner and your only goal is to get some soft of exposure to a particular framework, then fine - please continue. If you have any sort of ambition towards actually understanding the framework, then please heed my advice - learn the fundamentals first.

Remember - [Rails is definitely not for beginners](http://rob.yurkowski.net/post/17610425880/rails-is-definitely-not-for-beginners). In fact, in the linked post, the author mentions my single favorite piece of advice for aspiring Rails devs:
>[L]earn how to write a Ruby program. That’s not hard—actually, I maintain that learning rudimentary Ruby is easier than learning pretty much any other programming language. You don’t have to be a genius or understand the implementation of the language to be able to write a basic script. You might need a bit more understanding to get good at it, but the issue is that many people fail to reach even this point, where they have basic proficiency.

There are at least two benefits to learning and understanding Ruby before going anywhere near Rails. The first, obviously (and as the author points out), is that learning Ruby will give you a basic understanding of the language Rails uses (and, let's face it, Rails is pretty much useless if you don't understand Ruby). The second is that Rails adds some nifty helper methods to stdlib Ruby classes - learning Ruby first will help you understand what those methods are and how to avoid confusion later on when you try to use a Rails-only method in a non-Rails application.

So what is my recommendation? How should beginners go about learning their framework of choice?

1.  Learn the fundamentals. This includes basic CS ideas and your language of choice. Do not just jump into the framework and hope for the best.
2.  **<strike>???</strike>** Then, and only then, start to learn the framework. Trust me, you'll thank me.
3.  Profit.

What I find interesting about the anecdote I opened this post with is that it's a commentary on the culture of "now" we have developed. People want to achieve their end-goal immediately - as soon as they discover that doing so will take more work and effort than they had hoped, they become disinterested. Aspiring Rails-devs-to-be have it a little easier, what with the countless courses and tutorials offered online and in-person. But that doesn't change the fact that people may be handicapping themselves by taking these shortcuts.
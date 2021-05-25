<!--
.. title: Why Computers Work: An Introduction to Following Rules
.. slug: why-computers-1
.. date: 2021-05-24 08:50:00 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Nicholas H.Tollervey
-->

<style>
.section_break {
    border: none;
    border-bottom: 1px solid black;
    width: 50%;
    color: #333;
    overflow: visible;
    text-align: center;
    height: 5px;
}

.section_break:after {
    background: #fff;
    content: '§';
    padding: 0 4px;
    position: relative;
    top: -13px;
}
</style>

## Why Computers Work (part 1) 

This is the first of five short blog posts exploring _why computers work_.

I'm going to present a friendly introductory overview for laypeople, from zero
to Turing machines, automata, abstraction and more. My aim is conciseness and
clarity, so I've necessarily missed out, glossed over and simplified things.
There are plenty of more advanced resources online should you wish to
investigate this subject further.

Most importantly, I hope to stimulate your thinking about computers by creating
a place to explore ideas.

I hope you enjoy these articles and, as always, I love getting constructive
feedback [via email](/contact). Unless otherwise stated, all images and
diagrams were created by the author.

<hr class="section_break"/>

> αἰὼν παῖς ἐστι παίζων, πεσσεύων· παιδὸς ἡ βασιληίη.
>
> (The universe is a child's game. A child's kingdom.)
>
> ~ [Heraclitus](https://plato.stanford.edu/entries/heraclitus/) (Fragment B52)

## Introduction

Computers are ubiquitous.

They touch all aspects of our lives, from mediating our social interactions to
modelling aspects of our culture and managing the everyday infrastructure of
society.

<p>Therefore, computers are interesting and, understandably, folks want to
know <strong>how</strong> the machines that automate and control so much of our world work.
<a href=" https://www.youtube.com/watch?v=tpIctyqH29Q" target="_blank">This is
a typical response</a>.</p>

I'm going to take a different approach.

I'm going to explore **why** computers work.

What's the difference?

Answers to "how?" questions tell us what method or steps make something happen.
In contrast, the answers to "why?" questions describe what makes something
possible ~ an opportunity to encounter a more fundamental perspective.

It's the difference between a car mechanic who may understand *how* an engine
works (so they can fix broken engines), and a mechanical engineer who
understands the physics and chemistry relating to *why* engines work (so they
can improve the design of engines). Knowing how something works means your
frame of reference is *within the system*, whereas if you understand why
something works you're not bound by existing products, solutions or cultural
practices.

Most importantly, cultivating an understanding of why something is possible is
an invitation for playful creativity, fearless exploration and careful
refinement of alternatives to the current crop of answers to "how?". It is an
opportunity to enlarge and change our world ~ a form of intellectual
empowerment and growth.

Knowing _how_ is good, but understanding _why_ is better.

With the scene suitably set, to start our journey, we'll learn all about...

## Following Rules

Do you know how to play the children's card game, Snap?

(Bear with me, I promise it'll be worth it.)

Using a standard deck of cards, the aim is to win all the cards by _taking
turns to play_.

Let's follow along as siblings Penelope (11), Sam (8) and Will (5) play a game:

Penelope (for no other reason than she's the oldest) acts as dealer. She
shuffles the deck of cards so they're in a random order and deals them, face
down and in equal quantity, to each player until there are none left to deal.
This is the starting state from which all games of Snap begin.

Sam, the player to the left of the dealer, takes the first turn.

Players take a turn by moving the top card from their face-down stack onto the
top of an adjacent stack of face-up cards, so the newly moved card is also
facing up. Since this is Sam's first turn, the face-up stack doesn't exist,
so a new stack is created with Sam's first face-up card taken from his pile of
face-down cards.

So ends Sam's turn.

<figure>
<img src="/images/snap.jpg" alt="A game of Snap!"/>
<figcaption>
  <a href="https://www.wikihow.com/Play-Snap" target="_blank">Source</a> - From
  <a href="https://www.wikihow.com" target="_blank">WikiHow</a> and licensed
  under
  <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en" target="_blank">CC BY-NC-SA 3.0</a>
</figure>

The next player to the left, William, takes his turn in a similar fashion and
so the game continues from one player to the next.

After a while Sam shouts "SNAP". He's noticed that two face-up cards on top of
different stacks have the same value (for example, two aces are visible on top
of Penelope and Will's stacks). Since he was first to shout "SNAP" he wins all
the cards in the matching stacks of cards. He gleefully scoops up all the cards
in the face-up stacks belonging to Penelope and Will.

Play continues to the left of the player who turned up the matching card.

A few moments later Penelope shouts "SNAP". But there is a problem: there are
no matching face-up cards! William points this out to Penelope and reminds her
she has to pay a forfeit by giving one card to each of the other players from
her face-down stack. Sam and Will get a card each and Penelope is two cards
down.

At this point in the game Sam has the most cards. Will and Penelope have less
with only a few cards difference between the quantities in their face-down
stacks.

Things are hotting up and the three children become more excited: when two
matching face-up cards appear again all three of them shout "SNAP" at the same
time. Since nobody can claim to have shouted "SNAP" first, and to avoid
arguments, both the matching stacks are placed in the middle and added to the
"Snap pool". When "SNAP" is next called unambiguously and correctly, the winner
will get both the matching stacks and any cards in the "Snap pool". The stakes
have suddenly got higher.

Things quieten down for a few rounds until Penelope runs out of face-down cards
to put onto her face-up stack. At this point she simply flips over her face-up
stack and it becomes her face-down stack. Play continues as before.

Eventually, after a few more calls of "SNAP", Penelope finds that she's run out
of cards and so out of the game.

Sam and Will play together until, through luck and fast reactions, Sam finds
himself with all the cards and he's declared the winner of the game.

That's how you play Snap..!

<p id="rules_of_snap">The rules illustrated in this deliberately precise story describe
<em>how</em>, given certain states of affairs, such-and-such things must
happen. States of affairs unambiguously describe how things are in the world.
For example, "there are two stacks of face-up cards whose top cards are of
matching value". When I describe how such-and-such must happen, I mean clear
and unambiguous instructions describe <em>how</em> play proceeds given a
certain state of affairs.</p>

Put simply, this is *how* the game of Snap is played.

But *why* is Snap played?

Because, in addition to knowing the rules, we understand that playing the game
of Snap means modifying one's behaviour to follow these rules. If everyone
modifies their behaviour in accordance with the rules then folks can play
together. Obviously, we don't explain card games in such a formal manner to
very young children. But, as my description shows, children discover it's lots
of fun to informally learn and skilfully follow rules that bring about
exciting situations in games.

<p>Knowing how to play Snap is analogous to knowing how computers work. Looking
beyond the rules of Snap to appreciate that human behaviour and enjoyment
motivates people to follow the rules of the game, shows us <em>why</em> Snap is
played. This insight may also inspire us to invent new games. Perhaps we become
inspired to explore further aspects of
<a href="https://en.wikipedia.org/wiki/Milgram_experiment" target="_blank">human behaviour relating to following rules</a>,
or we may even
<a href="https://theoryoffun.com/" target="_blank">reflect upon the nature of play or games</a>.
In any case, exploring <em>why</em> rather than <em>how</em> provides a
fascinating perspective from outside the system (of Snap, in this case).</p>

We need to achieve an analogous enlargement of perspective beyond _how_
computers work in order to understand _why_ computers work. Only by acquiring a
perspective outside current norms can we possibly hope to invent or improve
technology and explore the nature and use of such devices. The alternative is
churn and recycling of existing ideas within the current system ~ a situation
that stifles innovation or positive change.

The computing-related rules and states of affairs I'm going to describe are not
much more complicated than the game of Snap explained above. However, what
follows may include a few *brain twists* where I expect you to use your
imagination to see things in a seemingly unusual or unintuitive way! I'm
challenging you to acquire a new perspective about seemingly everyday things.
The external world remains as it was before, but you will have changed. Your
newly acquired perspective reveals a deeper understanding of what you're
observing and why this makes computing possible. It's fun and can result in
rather pleasant "aha" moments (if you were a cartoon character, it's that
feeling you get when a lightbulb appears above your head).

The next chapter in our story is a beautiful brain twist: to think about
thinking...

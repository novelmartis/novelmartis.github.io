---
layout: post
title: Neural Networks
tags: [2025, explainer]
description: The why, how, and what.
comments: true
---

A simple explainer into why we build neural networks, how they learn, and what they mean for the rest of us, as narrated by ChatGPT o3 (with a LOT of prodding). If you want a technical introduction to Neural Networks, I recommend Michael Nielsen's [online book][mn_link].

<hr>

![Illustration]({{site:url}}/assets/nn_blog.png)

#### A tiny everyday puzzle

Imagine a quiet side street at dusk. Your smart garage door is supposed to close only when **your** car has fully rolled in, stay open for your partner’s bike, and never squash the neighbour’s cat.
With a handful of clear-cut cases—“car sensor on → close; car sensor off → open”—you can write a crisp rule-based program. But the real alley is messy: shadows wobble, bikes glide halfway in, a delivery van idles across the sensor beam. To handle the chaos you’d have to lay down an impossibly long checklist of if-this-then-that rules and update it every time the world invents a new edge case.

That is the moment you start craving a different kind of software—one that **adapts** from examples rather than follows a frozen playbook. In that craving lies the seed of machine learning.

#### From hand-written rules to learned lines

The gentlest form of learning is **linear regression**. Give the computer a scatter of points—say, month of the year on the x-axis and the supermarket price of strawberries on the y-axis—and ask it to draw the straight line that best threads through them. The slope and intercept become a tiny "program" the model has written for itself:

```
price ≈ 4.2 €  –  0.15 € × month
```

That humble line already beats a rule list because you never typed the numbers; the algorithm inferred them. Grocers can now order crates a month ahead without eyeballing every invoice.

But strawberries behave politely. Mangos, avocados, petrol, stock prices, and teenage growth spurts do not. Their curves dip, spike, or plateau in ways a straight line can’t follow. We could bolt on manual fixes—split the year into seasons, add a polynomial, toss in a “Christmas surge” term—but each bolt is another handwritten assumption. Eventually the patchwork collapses under its own specificity.

We need an engine that can *sculpt* any curve the data whispers, by itself.

![Examples of machine learning algorithms]({{site:url}}/assets/nn_eg.svg)

#### Enter the neuron

Simple artificial "neurons" carry out two tricks:

1. **Add**. Multiply each incoming number by a weight and sum them up.
2. **Squash**. Pass that sum through a gate called an activation function. The most-used gate is ReLU (Rectified Linear Unit): *If the sum is positive, keep it; else zero it*.

That simple gate is deceptively powerful. Chain together a handful of neurons in a **layer**, feed the outputs of one layer into another, and the network can bend straight lines into gentle S-curves, jagged cliffs, or anything in between. No matter how twisty the underlying relationship, enough neurons can approximate it. This universal-approximation property is why neural networks have become the Swiss Army knife of function fitting.

A nice symmetry pops out here: if you *remove* every kink—replace all the gates with identity functions—a single-layer network collapses right back to linear regression. So neural nets are not mystical departures from classical stats; they are linear models with an unlimited supply of bends. How we make those bends obey our needs?

#### How the bends learn to bend

Learning is just weight-tweaking. Each time the network makes a prediction, we compare it to the truth, measure the error, and ask a now-famous algorithm called back-propagation to levy blame:

*"Output neuron, you were off by +2. Hidden neuron #3 contributed 20% to that mistake, so nudge its weights downward accordingly; hidden neuron #4 contributed −5%, so bump it up,”* and so on.

Run this blame-and-tweak loop over thousands of examples, and the weights settle into values that slash the overall error. Back-prop is often caricatured as heavy calculus, but at heart it is a glorified chain rule mixed with bookkeeping—a way to send the "fix the leak" message to the precise pipes responsible.

#### Helping the network with our prior hunches

Sometimes we do have a hint about how the data is structured:

- **Images**: neighbouring pixels usually belong to the same object. Convolutional Neural Networks (CNNs) hard-wire that local-patch assumption.
- **Language and audio**: the next word or sound depends on the ones just spoken. Recurrent Neural Networks (RNNs) loop information forward in time.
- **Molecules, social graphs, road maps**: items connect in webs, not grids. Graph Neural Networks keep track of those links.

By baking the hint into the architecture, we save the model from relearning obvious facts and let it spend its capacity on the subtler patterns.

#### Transformers and the "predict-the-next-token" game

Taking our hints to the frontier, the rock-star architecture of the past few years is the **Transformer**. It discards convolutions and recurrence in favour of self-attention: every word in a sentence can look at every other word in one shot and decide how much it cares - *discover the connections you needs*. Training boils down to the laziest game in AI: "given the text so far, guess the next chunk." Feed the system the open web—Wikipedia, Reddit, arXiv, cooking blogs—and the network must absorb grammar, facts, styles, and a surprising slice of reasoning simply to stay good at the game.

Scale that recipe and you get today’s ultra-expressive large language models. ChatGPT, launched near the end of 2022, broke every growth chart, crossing a hundred million users faster than TikTok or Instagram. For the public, it was a jolting reminder that neural nets are no longer lab curiosities; they are turning into everyday companions.

#### But what exactly did the model learn?

Pop open a Transformer and you meet billions of weights—far too many for human inspection. Researchers now poke these models the way cognitive scientists probe brains:

- *Behavioural tests*: Can it count syllables? reason about physics? follow ethical constraints?
- *Mechanistic digs*: trace little circuits dubbed induction heads that spot patterns like “A…B…A → predict B,” an algorithm useful for copying, translating, even doing simple logic.

The digs reveal flashes of structure but also expose fragility. Slightly rephrase a prompt and the same model that solved your logic puzzle might hallucinate a reference or mis-quote a statistic. Flexibility and interpretability remain a trade-off we have not fully solved. Currently, as the internal processes of these networks are hard to understand, to assess the "trustworthiness" of their capacities, we mostly fall back to *behavioural auditing*—test them the way we test pilots or surgeons: repeated drills, stress cases, constant monitoring.

#### Beyond the glitz: Where neural nets (might) live and affect you

- **Hospitals**: CNNs can highlight tumours in MRI scans within seconds, helping radiologists catch early cancers—but regulators demand rigorous validation because a missed pixel can cost a life.
- **Highways**: driver-assist systems lean on vision networks to track lanes and spot pedestrians; a handful of tragic crashes underscore why "mostly works" is not good enough for safety-critical gear.
- **Video games**: non-player characters (NPCs) now hold fluid conversations and adapt their strategies mid-match, thanks to language-driven planning models.
- **Scientific labs**: protein-folding networks predict 3-D structures that once took months of crystallography, speeding up drug discovery.

Notice a pattern: wherever the environment is too fuzzy for rule lists, neural nets creep in. Of course, they aren't just everywhere because many of these domains require us to "explain" why one does what one does, which is hard to extract from neural networks.

#### So, should you trust them?

Broadly, "trust" is perhaps a limiting lens; *Literacy* is more important. You don’t "trust" electricity—you learn its rules enough to wire a lamp safely. Neural networks are becoming a similar infrastructure layer. The people who grasp even the rough outlines of how they fit curves, how they can surprise you, and where they tend to fail will be better equipped to build on them, critique them, or simply use them wisely.

That said, another camp is working on something deeper: can we bring the networks’ internal logic closer to how human brains reason, so that the everyday notion of “trust”—the way you trust a seasoned pilot—starts to apply to future AI *agents*? Projects that compare neural activations to brain recordings, or weave symbolic reasoning into deep neural networks, are early steps on that path. 

Whether that brain-alignment research pans out or not, the order of operations stays the same: **first we cultivate basic AI literacy, then—after rigorous, transparent testing—we can grant the system genuine trust**.

#### A short parting checklist

- Hand-written rules crumble in a messy world.
- Linear regression writes its own tiny rule—but only straight lines.
- Neurons plus kinks give us curves on demand; back-prop teaches them.
- Clever architectures bake in domain hints (CNNs, RNNs, Transformers).
- More flexibility → less interpretability, so we audit behaviour and dig for circuits.
- From medical imaging to chatbots, neural nets are poised to shape daily life.
- Understanding the basics lets you harness the magic without buying into the hype.

That, in the end, is the point of this post: not to crown neural networks as artificial minds, nor to dismiss them as inscrutable black boxes, but to hand you the conceptual map so you can wander the territory with your eyes open. Your next build/question will be on firmer ground.

[mn_link]: http://neuralnetworksanddeeplearning.com/
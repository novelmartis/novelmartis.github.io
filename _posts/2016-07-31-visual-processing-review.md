---
layout: post
title: Visual infomation processing with biologically-realistic neural networks - Musings
tags: [2016, vision, snn]
description: Introduction to the line-of-attack
comments: true
---

## Introduction

Vision for us is so natural, rapid and effortless. But how do we recognise a cat as a cat? We might be identifying multiple features such as its ears, its nose, its shape and size. We might have a template for a cat in our brains, with which we match the input image. Template matching sounds promising but is a procedure that is ridiculously complex. For example, what would the template of a cat contain, and how would the images in the figure below be comparable to that template? 

![Template of a cat?]({{site:url}}/assets/cats_all.png 'Template of a cat?')

There are two routes to go from these images to the template:

1. Non-linear 3D spatial transformations and non-linear transformations on color intensities.
    - Distorting the image and changing the color profile to fit the template.
2. Recognise individual features (ears, eyes, etc.) in those images and build the template using them.

The first route can encompass the second, as individual feature recognisers could be treated as non-linear transformations on the pixel map. Handpicked features do not provide optimal performance, making the first route the choice for exploring visual information processing. 

We might be employing a complex template matching approach, but stating that isn't enough. How do we implement these non-linear transformations? How does a network of neurons implement object recognition? This problem is being solved using the mathematical, algorithmic and neuroscience perspectives. The objective is to understand how a biologically-realistic neural network could implement visual information processing.

This could be a line-of-attack: <br>

```
Visual information processing with biologically-realistic SNNs
├── The problem
├── Previous Work
│   ├── Outline
│   ├── Computer Vision
│   │   └── CNNs, RNNs, etc
│   ├── Biological Modelling
│   │   └── HMAX, etc
│   ├── SNNs
│   └── Additions to the problem
│       └── Unsupervised learning
├── Working with SNNs
│   ├── Architectural constraints
│   │   ├── Operational principles: tight E-I balance, etc.
│   │   └── Neural models - Simplicity vs Accuracy
│   └── Learning Rules
│       ├── ReSuMe, etc
│       ├── Backpropagation modified?
│       └── Other rules? - Explore
└── Further work
    ├── Deciding the learning rules
    └── Generalising to videos, attention, etc
```
---
layout: post
title: Current Debates Essay plan
tags: []
description: Meta. Not for the website.
comments: false
---

```
Visual infomation processing with biologically-realistic SNNs
├── Introduction to the problem
├── Previous Work
│   ├── Outline
│   ├── Computer Vision
│   │   └── CNNs, RNNs, etc
│   ├── Biological Modelling
│   │   └── HMAX, etc
│   ├── SNNs
│   ├── Ruminations
│   └── Additions to the problem
│       └── Unsupervised learning
├── Working with SNNs
│   ├── Outline
│   ├── Architectural constraints
│   │   ├── Operational principles: tight E-I balance, etc.
│   │   └── Neural models - Simplicity vs Accuracy
│   └── Learning Rules
│       ├── ReSuMe, etc
│       ├── Backpropagation modified?
│       └── Other rules? - Explore
└── Concluding Remarks
    ├── Deciding the learning rules
    ├── Generalising to videos, attention, etc
    └── Other comments
```

## Details:

### Introduction
- Going from pixels to features, simplest version (full version has motion, overt attention, top-down biases, etc.)
- Turns out to be a hard problem
- Humans do it effortlessly and rapidly
  - We would like to to understand how, so SNN models required

### Previous Work
#### Outline
#### Computer Vision
- Early attempts (Clustering, k-means, SVMs)
  - Category grouping requires lots of non-linear transformations
  - Locally-correlated information, towards the idea of receptive fields
- Convolutional Neural Networks
  - Incorporating the idea of receptive fields and hierarchical feature-extraction
      - Learnt through backprop
  - Exhibit striking results with good features (and 'hidden' features)
  - Exhibit high correlation of information representation with hVS fMRI data
  - Further work (with RNNs to do attention task and multi-object processing - bounding boxes)

#### Biological Modelling
- Idea of receptive fields in V1, gabor identification, color and shape specificity, face and body areas.
- Putting it all together - HMAX (simple and complex cells with receptive fields)

#### Spiking Neural Networks
- Biological neuron models
  - HH, then simplifications: Izhi, AEIF, etc.
  - Simplifications capture spike times, and adaptation, but not the AP profile, which is a good starting point
- Visual processing with SNNs
  - No idea: EXPLORE, FIND OUT
  
#### Rumination
- Sigmoid neurons and spiking neurons are fundamentally different, but atleast we have guidelines.
- Receptive fields and hierarchies in CNNs are partially motivated by the human visual system, but are they a fundamental computational principle, as suggested by local correlations?
- We need to understand SNNs better to translate CNN-like structure to them.
- Feedback management, operational conditions, learning rules.

#### Additions to the problem
- Unsupervised feature learning is key - children, during development, do not have access to semantic information. How do they still cluster similar objects together (or do they, without being told so?)
  - Can we train an unsupervised ANN to do object recognition, and then one-shot label learning?
  - Can evolutionary algorithms like NEAT work out here - if you initialise a fully connected network, would it acquire the structure of CNNs?

### Working with SNNs
#### Outline
#### Identifying Architectural Constraints
- Operational Principles
  - tight E-I balance, FIND MORE
- Information Coding principles
  - Rate Code
  - Rank Order Code
  - Spike-time codes, other codes, FIND OUT

#### Learning Rules
- Previous Neural Learning models
  - ReSuMe
  - FIND OUT MORE
- Modifying backprop?
  - SpikeProp
  - Bengio's bio-backprop (TO READ), FIND MORE
  - The paper where they made the SNN activation function continous for backprop.
  - My suggestions
- Other rules? FIND OUT

### Concluding Remarks
- Deciding the learning rules
- Building the SNN
- Onwards to unsupervised learning - why is unsupervised learning harder, or is it?
- Generalising to videos, attention, etc (with RNNs, or SNNs)
- Other comments




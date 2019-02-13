---
layout: post
title: Quadcopter control using Spiking Neural Networks
tags: [thesis, 2015, snn, quadcopter, show-all]
description: Rumination over my Bachelor's thesis project, which was left incomplete partly by a roadblock.
comments: true
---

*This one dates back to 2015. This was the topic of my bachelor’s thesis, which was admittedly left incomplete. Find the report [here][thesis].*

[Spiking Neural Networks][snn] hit that sweet spot between biological neural networks and artificial neural networks (although now [RNNs][rnn] and [CNNs][cnn] are struggling to take over). To better understand how they function, we thought about using them to solve a well-known complex control problem - balancing and flying a quadcopter. 

The first step was to understand quadcopter flight dynamics. The quadcopter is inherently an unstable system - the smallest uncorrected angular deviation in pitch can send the quadcopter flying out of control. PIDs (compensatory mechanisms that worked by controlling the four rotors) were simple and efficient solutions to this problem. In the first leg of the project, we designed a control algorithm directly taking the dynamical equations of the system into account. Our algorithm outperformed [PID][pid]s, and could recover the quadcopter from a multitude of states (including crazy upside-down states). 

Having understood quadcopter dynamics, we wanted to move ahead to bring in the SNNs. The roadblock was severe. How were we supposed to use SNNs to fly a quadcopter? There were multiple options -

1. Learning algorithms such as [ReSuMe][resume], 
2. Evolutionary methods such as [NEAT][neat],
3. Hand-assembling a network,
4. Understanding a natural control system such as the cerebellum and trying to re-purpose the mechanisms. 

(4) is a hard problem, but would definitely be interesting to address someday. We weren’t aware if somebody had used (1), but I wasn’t really impressed by the method. Also, the training would require data from the control system we developed, and we were not sure if the the algorithm would generalise and ‘go beyond’ - which would be the point of using a learning algorithm. (But maybe the ‘i-dont-like-it' factor weighed heavier) (2) was used in a [paper][neat-quad] successfully, but not with SNNs (NEAT with SNNs is a computationally-heavy routine).

So, were we supposed to hand-assemble the network? That sounded sour. But then my advisor hinted at building plug-and-play spiking network modules which could be assembled to emulate any control algorithm. We were focussed on the basic arithmetic operations - addition, subtraction, multiplication and division - which mostly are sufficient for implementing simple control systems. Also, the control algorithm we designed in the first leg of the project used only polynomial operations. So, we set out on this path, and we came up with a method which lets one implement any polynomial transform on real-time spike trains, and [published a paper][ijcnn] about it. (I will discuss the details in another post)

It so turned out that the time lags involved in the more complex operations such as multiplication of variables raised to some power, were huge. It became extremely hard to combine the modules we designed to emulate the control algorithm we had built. By that time, my time at IIT Bombay was up, and the project was left unfinished. As tempting as the approach sounded, I now think that it wasn’t the best way to proceed.

It would be interesting to get around the time lag problem, but I’d put my bets on another approach. In any case, it was an awesome experience trying to bend SNNs to our will - seems we lost.

[thesis]: https://dx.doi.org/10.6084/m9.figshare.1582657.v1
[snn]: https://en.wikipedia.org/wiki/Spiking_neural_network
[rnn]: https://karpathy.github.io/2015/05/21/rnn-effectiveness/
[cnn]: https://arxiv.org/abs/1605.07678
[pid]: https://en.wikipedia.org/wiki/PID_controller
[resume]: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.60.6325&rep=rep1&type=pdf
[neat]: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.28.5457&rep=rep1&type=pdf
[neat-quad]: https://classes.engr.oregonstate.edu/mime/fall2010/me537/Papers/NN_EA_application_shepherd.pdf
[ijcnn]: https://dx.doi.org/10.1109/IJCNN.2015.7280822

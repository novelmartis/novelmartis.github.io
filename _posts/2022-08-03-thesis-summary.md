---
layout: post
title: Ph.D. thesis summary
tags: [2022, thesis]
description: A short summary of my Ph.D. thesis titled "Smart Search".
comments: true
---

The thesis, "Smart Search: Investigations into human visual search in structured environments", presents studies on human visual search behavior and how the machinery of the human brain operates toward generating that behavior. The thesis has been approved for defense by the review committee and further details can be found [here][defense_link].

<hr>

![Illustration]({{site:url}}/assets/dalle_thesis.png)

Consider visually searching for an object of interest. If we do not know where that object is we need to look around until we see that object. We do not look around haphazardly though. Let’s think about the routines we use in looking around. Even though we do not know where the object is, we could know where the object could be. For example, while searching for a book at home, it is most likely on the table and not on the floor or the ceiling. This knowledge can help us avoid many locations in the scene, thereby quickening our search. Another routine involves how the object looks. It is easier to look away from a location that contains an object that looks very different (differing features) than the object of interest.

Relatedly, through behavioral experiments, researchers found out that such feature-based comparisons can occur simultaneously throughout our field of view, without the explicit need to move our eyes or our "spotlight of attention" to the various objects. For example, the speed of search for a blue ball among red balls is independent of the number of red balls in view. However, the search for a blue ball among red balls and blue boxes depends on the number of balls and boxes. This is because we can compare throughout our visual field based either on the color or the shape but not both at once. This process of parallel comparison is called feature-based attention.

One of the questions addressed in this thesis is about what features can avail of such parallel comparison. Although the features of color and shape cannot be combined into a feature that can avail feature-based attention, researchers found that other feature combinations, such as motion direction and color, can be combined into a feature that can avail feature-based attention. It is currently thought that feature combinations that specifically activate neurons in the brain can avail feature-based attention. For example, there are no neurons that specifically respond to the presence of a blue ball but there are neurons that specifically respond to blue dots moving to the right. The question we made headway into in <b>Chapter 2</b> of the thesis was whether another combination of features that selectively activate neurons, body shapes, also avail feature-based attention. We also assessed whether other shapes such as cars and lamps can also avail feature-based attention.

For these assessments, we used functional magnetic resonance imaging (fMRI), a method used to infer neural activity in response to a stimulus by recording the associated blood flow to those neurons. Participants searched for body and the other shapes in two vertically-aligned boxes. We analyzed the activity of neurons that specifically respond to body shapes presented in two horizontally-aligned boxes. When participants were searching for bodies, the neural response to bodies was higher than the neural response to the other shapes. This response difference was higher during the search for bodies than in the search for the other shapes. These results suggest that even in the locations where bodies are not to be detected, bodies are detected easier when bodies are the search targets elsewhere. This is a signature of feature-based attention, where bodies are the features. Such signatures were not found for the other shapes. Thus, in <b>Chapter 2</b>, we found evidence, supporting previous research, that body shapes can avail feature-based attention in human visual search. Whether bodies, in addition to faces, are special shapes that are highly ecologically relevant and therefore avail feature-based attention more prominently than other shapes such as cars or lamps, is a topic for further research.

In addition to feature-based attention modulating how the feature-selective neurons respond based on the target of visual search, it has also been proposed that such modulation might occur throughout visual processing. Objects can have multiple differing features, at various levels of visual processing. While beds and cars have different shapes, they can also be differentiated based on the overall orientation of their edges - cars have more horizontal edges than beds do. Such orientations specifically activate neurons in the early parts of the visual processing hierarchy in the brain. However, it is believed that the modulation of neurons at the earlier parts incurs a higher metabolic cost than the modulation of neurons at the later parts. This is because the point of origin of target-driven modulations lies anatomically (and conceptually) closer to the later parts. However, a question arises: when does it become essential that the target-based modulation be directed at the earlier parts of visual processing in addition to the later parts?

In <b>Chapters 3</b> and <b>4</b>, we addressed this question using computational modeling with artificial neural networks (ANNs) - a class of algorithms inspired by the networks of the brain. We reasoned if the information relevant to the task at hand is available at the later parts of the hierarchy, then any filtering of information through modulation at the earlier parts would not add anything. Whereas if that information is not available, for example, due to the network being small given the task i.e. having a lower capacity, then modulation of the earlier parts might route the relevant information to the later parts leading to better task performance. To test this hypothesis, we trained an ANN to perform cued tasks - given an image, the network had to output whether a cued object was present in the image. The cue was either provided as a modulation of the late layer of the ANN or both of the early and late layer of the ANN. The capacity of the ANN was a function of the number of neurons and the number of categories that could be cued. We found that the modulation of the early layer was only helpful when the capacity of the ANN was low i.e. it had a low number of neurons given the number of categories. This modeling approach also raised several questions. For example, how are the base network and the modulation trained in the brain: is the modulation trained after the base network is trained or are they trained together, during development?

A third routine we use in looking around during search relates to the relationships between objects in the world. Objects have spatial co-occurrence and semantic relationships. For example, a TV stand appears more often with a TV, with the TV on top of it, as compared to appearing with a car. These relationships influence our search. In searching for a TV in a blurry scene, the presence of a TV stand provides us with more confidence. Relatedly, it has been proposed that co-occurring objects are grouped, effectively making them one big object in our view. An interesting consequence of this phenomenon could be that environments containing co-occurring objects could be easier to search through as the effective number of objects to be assessed in finding the target would be lowered due to grouping.

In <b>Chapter 5</b> we assessed the possibility of improving search efficiency in the presence of co-occurring objects. Participants searched for cued shapes in displays that contained either co-occurring (structured scenes) or non-co-occurring distractor shapes (unstructured scenes). The co-occurring distractors occurred in pairs of two with either the relative positions of the shapes within the pairs being fixed or free (in separate experiments). After some training runs, we observed that participants were both faster and more accurate at indicating the location of the cued shape in the structured scenes. We also found that this benefit in the search did not depend on whether the relative positions of the shapes in the pairs were fixed or free. The grouping-based account cannot readily explain the benefit in search for the free arrangement case unless we assume that twice as many groups were registered with no detriment to the benefit in search. We proposed an alternate account where the relationships between the co-occurring shapes could quickly help reject the partner shape when one of the shapes was identified. Whether such a process can happen in parallel across the visual field or has to proceed sequentially through the distractors, and how relevant such a process might be during visual search in the real world are topics for further research.

In <b>Chapter 6</b>, we assessed the neural processes underlying the observed benefit in search, using electroencephalography (EEG), a method used to infer neural activity by recording electrical potentials on the scalp. We assessed the differences between the averaged electrical potentials from the onset of structured and unstructured scenes. For both the scenes, around 200-400 milliseconds after display onset we observed a larger deflection over the hemisphere opposite to the side where the cued shape was present than the hemisphere on the same side as the target. This difference, termed the N2 posterior contralateral (N2pc) component, is a signature of increased attentional orientation towards the target. We found that the N2pc difference between the structured and unstructured scenes was found to be larger in participants showing a higher benefit in search amongst the co-occurring distractors. This effect suggested that the observed benefit in search could be attributed to rapid attentional orientation, and not later decisional processes. However, this effect was weak and needs to be interpreted with care. Further experiments, employing other methods such as fMRI, are necessary to understand the mechanisms underlying the benefit in search due to co-occurring distractors.

In this thesis, in the spirit of computational cognitive neuroscience, we peeked under the hood of the routines we employ in visual search, to further understand how the human brain uses its machinery to execute those routines. These investigations involved the use of highly controlled, artificial stimuli to isolate the effects of interest in answering the questions posed. However, as outlined above, further experiments are essential to know if the observed/postulated processes are indeed at work during our search in the real world. This thesis serves as another small step towards unraveling the workings of the human brain that underlies all the mind-boggling behavior produced on this mote of dust suspended in a sunbeam.

[defense_link]: http://sushrutthorat.com/thesis-defense
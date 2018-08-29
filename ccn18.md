---
layout: float_page
title: The function of cue-driven feature-based feedback in object recognition
---
(Paper accepted at [CCN-2018][ccn])

Authors: Sushrut Thorat, Marcel van Gerven, Marius Peelen

<b>Resources:</b> [Paper][ccn18] ([Reviews & Replies][ccn18-rev]), [Poster][poster], [Code][git_c]
<hr>

<b>Abstract:</b> 

Visual object recognition is not a trivial task, especially when the objects are degraded or surrounded by clutter or presented briefly. External cues (such as verbal cues or visual context) can boost recognition performance in such conditions. In this work, we build an artificial neural network to model the interaction between the object processing stream (OPS) and the cue. We study the effects of varying neural and representational capacities of the OPS on the performance boost provided by cue-driven feature- based feedback in the OPS. We observe that the feedback provides performance boosts only if the category-specific features about the objects cannot be fully represented in the OPS. This representational limit is more dependent on task demands than neural capacity. We also observe that the feedback scheme trained to maximise recognition performance boost is not the same as tuning-based feedback, and actually performs better than tuning-based feedback.

<hr>

[ccn]: https://ccneuro.org
[ccn18]: https://ccneuro.org/2018/proceedings/1044.pdf
[ccn18-rev]: http://sushrutthorat.com/assets/ccn18-reviews-response.pdf
[git_c]: https://github.com/novelmartis/cue-feedback-ccn18
[poster]: https://doi.org/10.6084/m9.figshare.7012316.v1

{% include  disqus.html %}
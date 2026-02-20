---
layout: page
title: Research
permalink: /research/
---

# Research

<p class="muted">
I build learning systems shaped by biological constraints—developmental curricula, active sensing, recurrent computation, and continual adaptation—and validate them against behavior and neural measurements.
</p>

<!-- <div class="linkrow">
  <a class="btn" href="https://scholar.google.it/citations?user=MPFzJQgAAAAJ&hl=en">Google Scholar</a>
  <a class="btn" href="https://figshare.com/authors/Sushrut_Thorat/522624">figshare</a>
</div> -->

<hr class="hr">

<div class="work-controls" aria-label="Work controls">
  <button class="btn" type="button" id="workExpandAll">Expand all</button>
  <button class="btn" type="button" id="workCollapseAll">Collapse all</button>
</div>

<script>
  (function () {
    const groups = () => Array.from(document.querySelectorAll('details.projgroup'));
    const setAll = (open) => groups().forEach(d => (d.open = open));

    document.getElementById('workExpandAll')?.addEventListener('click', () => setAll(true));
    document.getElementById('workCollapseAll')?.addEventListener('click', () => setAll(false));
  })();
</script>

<script>
  (function () {
    const nav = document.querySelector('header, .site-header, nav');
    if (!nav) return;
    const h = nav.getBoundingClientRect().height;
    document.documentElement.style.setProperty('--nav-h', `${Math.ceil(h)}px`);
  })();
</script>


<details class="projgroup" open>
  <summary>
    <span class="sumtitle">
      <span>Active perception and world modeling</span>
      <!-- <span class="daterange">1 flagship</span> -->
    </span>
    <span class="projmeta">sampling + prediction + control</span>
  </summary>

  <div class="projlist">

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Sequence model interpretability</p>
          <div class="ptitle">Emergent path integration and binding through sequential prediction</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/linda-proj.png" alt="World-Model">
        <div>
          <p class="pmeta">
            With: <a href="https://www.linkedin.com/in/linda-ariel-ventura-01a281158/"><u>Linda Ventura</u></a>, <a href="https://scholar.google.com/citations?user=P7Ly864AAAAJ&hl=en&oi=ao">Victoria Bosch</a>, <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            Predicting the next input encodes relational structure amongst the inputs: a RNN path integrates and binds the input tokens to their absolute locations in 2D scenes, in-context.
          </p>
          <div class="plinks">
            <span class="btn primary btn-disabled" aria-label="Ongoing">Ongoing</span>
            <a class="btn primary" href="https://arxiv.org/abs/2602.03490">Preprint 2026</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Scene representation</p>
          <div class="ptitle">Glimpse prediction for human-like scene representation</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/gpn.png" alt="GPN">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.ch/citations?user=YA6DPIcAAAAJ&hl=en">Adrien Doerig</a>, <a href="https://scholar.google.com/citations?user=hWKtP0sAAAAJ&hl=en&oi=ao">Alexander Kroner</a>, <a href="https://scholar.google.com/citations?user=ISe0qbAAAAAJ&hl=en&oi=ao">Carmen Amme</a>, <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            Predicting the next glimpse features (given the saccade) coaxes a network to encode co-occurrence and spatial arrangement in a visual-cortex-aligned scene representation.
          </p>
          <div class="plinks">
            <span class="btn primary btn-disabled" aria-label="Flagship">⭐</span>
            <span class="btn primary btn-disabled" aria-label="Ongoing">Ongoing</span>
            <a class="btn primary" href="https://arxiv.org/abs/2511.12715">Preprint 2025</a>
            <a class="btn" href="https://bsky.app/profile/sushrutthorat.bsky.social/post/3m5vqsdfug22t">BSky thread</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Controlling attention</p>
          <div class="ptitle">Assessing the emergence of an attention schema in object tracking</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/ast_schema.png" alt="Attention schema">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.com/citations?user=JNTzp6EAAAAJ&hl=en&oi=ao"><u>Lotta Piefke</u></a>,
            <a href="https://scholar.google.ch/citations?user=YA6DPIcAAAAJ&hl=en">Adrien Doerig</a>,
            <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            In cluttered object tracking with RL, an agent learns an explicit encoding of attentional state (an “attention schema”), most useful when attention cannot be inferred from the stimulus. 
            <!-- <i>Natural setting?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://escholarship.org/uc/item/1516x0js">CogSci 2024</a>
            <a class="btn" href="https://x.com/lolotta6/status/1815370164600246348">X thread</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</details>


<details class="projgroup">
  <summary>
    <span class="sumtitle">
      <span>Feedback and recurrent computation</span>
      <!-- <span class="daterange">1 flagship</span> -->
    </span>
    <span class="projmeta">time, inference, correction</span>
  </summary>

  <div class="projlist">

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Representational dynamics in RCNNs</p>
          <div class="ptitle">How does recurrence interact with feedforward processing in RNNs?</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/blt_arrangement.png" alt="BLT arrangement">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.ch/citations?user=YA6DPIcAAAAJ&hl=en">Adrien Doerig</a>,
            <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            The feedforward sweep instantiates a representational arrangement that dovetails with a recurrence-induced “equal movement” prior, enabling corrected classifications. 
            <!-- <i>Scaling? Feature highways?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://arxiv.org/abs/2308.12435">CCN 2023</a>
            <a class="btn" href="https://x.com/martisamuser/status/1712812776790311293?s=20">X Thread</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Decluttering due to recurrence</p>
          <div class="ptitle">Recurrent operations in neural networks trained to recognise objects in clutter</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/rnn-filter.png" alt="Recurrent flow">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.co.in/citations?user=qVvqArkAAAAJ&hl=en&oi=ao">Giacomo Aldegheri</a>,
            <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            Recurrent flow carries category-orthogonal feature information (e.g., location) used iteratively to constrain subsequent category inference. 
            <!-- <i>Scaling? Natural images?</i> -->
          </p>
          <div class="plinks">
            <span class="btn primary btn-disabled" aria-label="Flagship">⭐</span>
            <a class="btn primary" href="https://arxiv.org/abs/2111.07898">SVRHM@NeurIPS 2021</a>
            <a class="btn" href="https://twitter.com/martisamuser/status/1460631750640422912?s=20">X Thread</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</details>


<details class="projgroup">
  <summary>
    <span class="sumtitle">
      <span>Characterizing perception</span>
      <!-- <span class="daterange">1 flagship</span> -->
    </span>
    <span class="projmeta">representational structure, priors, and report</span>
  </summary>

  <div class="projlist">

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Ventral stream organization</p>
          <div class="ptitle">The nature of the animacy organization in human ventral temporal cortex</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/anim_proj.png" alt="Animacy organization">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.it/citations?user=5GQjAZkAAAAJ&hl=en&oi=ao">Daria Proklova</a>,
            <a href="https://scholar.google.nl/citations?user=v4CvWHgAAAAJ&hl=en">Daniel Kaiser</a>,
            <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            Animacy organization is not fully driven by visual-feature differences; it also depends on inferred factors like agency quantified behaviorally. 
            <!-- <i>Timecourse?</i> -->
          </p>
          <div class="plinks">
            <span class="btn primary btn-disabled" aria-label="Flagship">⭐</span>
            <a class="btn primary" href="https://doi.org/10.7554/eLife.47142">eLife 2019</a>
            <a class="btn" href="https://doi.org/10.6084/m9.figshare.5919154.v1">MSc thesis</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Priors in perceptual report</p>
          <div class="ptitle">Perception of rare inverted letters among upright ones</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/letter_illusion.png" alt="Letter illusion">
        <div>
          <p class="pmeta">
            With: <a href="https://www.linkedin.com/in/jochem-koopmans-051571236"><b><u>Jochem Koopmans</u></b></a>,
            <a href="https://scholar.google.com/citations?user=2ToC6n4AAAAJ&hl=en">Genevieve Quek</a>,
            <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            In a Sperling-like task, people report either occasionally-present or absent inverted letters as upright to the same extent => expectation-driven illusions may be post-perceptual, not p-conscious.
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://doi.org/10.1016/j.concog.2025.103964">ConsCog 2026</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</details>


<details class="projgroup">
  <summary>
    <span>Developmental constraints on learning</span>
    <span class="projmeta">learning history as an engineering prior</span>
  </summary>

  <div class="projlist">

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Infant visual diet</p>
          <div class="ptitle">Developmentally-inspired shape bias in artificial neural networks</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/dvd_b.png" alt="DVD: developmental shape bias">
        <div>
          <p class="pmeta">
            With: <b><a href="https://scholar.google.nl/citations?user=MnURMg0AAAAJ&hl=en&oi=ao"><u>Zejin Lu</u></a></b>,
            <a href="https://scholar.google.nl/citations?user=XZtcvyEAAAAJ">Radoslaw Cichy</a>,
            <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            Inspired by the <a href="https://www.sciencedirect.com/science/article/pii/S0273229724000017">Adaptive Initial Degradation hypothesis</a>, ANNs trained with a graded coarse-to-fine image diet produce strong shape-biased, plus distortion/adversarial robust classification behavior.
          </p>
          <div class="plinks">
            <span class="btn primary btn-disabled" aria-label="Ongoing">Ongoing</span>
            <a class="btn primary" href="https://arxiv.org/abs/2507.03168">Preprint 2025</a>
            <a class="btn" href="https://bsky.app/profile/timkietzmann.bsky.social/post/3lthef4bxu22c">BSky thread</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</details>


<details class="projgroup">
  <summary>
    <span>Adaptation and cognitive flexibility</span>
    <span class="projmeta">stability, plasticity, and rule switching</span>
  </summary>

  <div class="projlist">

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Rule inference in NNs</p>
          <div class="ptitle">Flexible rule learning in machines</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/winn.png" alt="Flexible rule learning">
        <div>
          <p class="pmeta">
            With: <a href="https://www.semanticscholar.org/author/R.-Sommers/114455459"><b><u>Rowan Sommers</u></b></a>,
            <a href="https://scholar.google.com/citations?user=YPdEhboAAAAJ&hl=en&oi=ao">Daniel Anthes</a>,
            <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            Inspired by <a href="https://openreview.net/forum?id=6orC5MvgPBK">Hummos</a>, we built an image-based Wisconsin Card Sorting Task variant and found behavior suggesting sparks of cognitive flexibility: compositional rule inference in activity space.
          </p>
          <div class="plinks">
            <span class="btn primary btn-disabled" aria-label="Ongoing">Ongoing</span>
            <a class="btn primary" href="https://arxiv.org/abs/2502.15634">Preprint 2025</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Continual learning and drift</p>
          <div class="ptitle">Structured representational drift aids continual learning</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/rdac.png" alt="Representational drift">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.com/citations?user=YPdEhboAAAAJ&hl=en&oi=ao"><b><u>Daniel Anthes</u></b></a>,
            <a href="https://scholar.google.nl/citations?user=Ieubd0EAAAAJ&hl=en&oi=ao">Peter König</a>,
            <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            Readout misalignment due to learning-induced drift is a core continual-learning problem. Constraining drift to the readout null-space helps networks stay both stable and plastic. 
            <!-- <i>Neural evidence?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://arxiv.org/abs/2310.04741">CoLLAs 2024</a>
            <a class="btn" href="https://2023.ccneuro.org/proceedings/0000748.pdf">CCN 2023</a>
            <a class="btn" href="https://x.com/AnthesDaniel/status/1717913109795410403?s=20">X Thread</a>
            <a class="btn" href="https://2024.ccneuro.org/pdf/567_Paper_authored_CCN2024-authored.pdf">CCN 2024</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</details>


<details class="projgroup">
  <summary>
    <span>Attention, search, and selection in scenes</span>
    <span class="projmeta">what gets amplified, where, and why</span>
  </summary>

  <div class="projlist">

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Modulation as routing</p>
          <div class="ptitle">Attentional Routing is as effective as Direct Access</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/ar_da_schema.png" alt="Attentional routing vs direct access">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.com/citations?user=z558t4EAAAAJ&hl=en&oi=ao"><b><u>Johannes Singer</u></b></a>,
            <a href="https://scholar.google.nl/citations?user=XZtcvyEAAAAJ">Radoslaw Cichy</a>,
            <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            Attentional routing can push task-relevant information through the network as effectively as “direct access,” challenging the necessity of direct access for explaining behavior. 
            <!-- <i>Neural alignment?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://2024.ccneuro.org/pdf/98_Paper_authored_submission_non_anonymous.pdf">CCN 2024</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Task-dependence of visual representations</p>
          <div class="ptitle">Task-dependent characteristics of neural multi-object processing</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/vs-neural.png" alt="Task-dependent multi-object processing">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.nl/citations?hl=en&user=3Fj2iKkAAAAJ"><b><u>Lu-Chun Yeh</u></b></a>,
            <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            The relation of multi-object display processing to isolated-object representations is task-dependent: same/different relates to earlier; object search, to later representations in MEG/fMRI. 
            <!-- <i>Mechanisms?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://doi.org/10.1523/JNEUROSCI.1107-23.2024">JNeurosci 2024</a>
            <a class="btn" href="https://x.com/LuChunYeh/status/1771482781337387299?s=20">X Thread</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Characterising search templates</p>
          <div class="ptitle">Size-dependence of object search templates in natural scenes</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/size-search.png" alt="Size dependence in search">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.nl/citations?hl=en&user=D0z0dcgAAAAJ"><b><u>Surya Gayet</u></b></a>, <a href="https://www.linkedin.com/in/elisa-battistoni-21597980/">Elisa Battistoni</a>, <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            Search templates encode identity and size; size is inferred from location in scenes, and is entangled with identity in the template. 
            <!-- <i>Computational model?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://psycnet.apa.org/doi/10.1037/xhp0001172">JEP:HPP 2024</a>
            <a class="btn" href="https://x.com/SuryaGayet/status/1763881177415364740?s=20">X Thread</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Implicitly learning distractor co-occurrence</p>
          <div class="ptitle">Statistical learning of distractor co-occurrences facilitates visual search</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/obj_grp.png" alt="Distractor co-occurrences">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.com/citations?user=2ToC6n4AAAAJ&hl=en">Genevieve Quek</a>,
            <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            Increased search efficiency amongst co-occurring distractors likely reflects faster/more accurate rejection of a distractor’s partner as a possible target. 
            <!-- <i>Mechanisms?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://doi.org/10.1167/jov.22.10.2">JOV 2022</a>
            <a class="btn" href="https://twitter.com/martisamuser/status/1518515944813101056?s=20&t=pACvyE-jT4DJB8SSwCdhaw">X Thread</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">High-level feature-based attention</p>
          <div class="ptitle">Bodies as features in visual search</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/bod-attn.png" alt="Bodies as features">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            Feature-based attention modulates fMRI representations of body silhouettes presented in task-irrelevant locations in high-level visual cortex. 
            <!-- <i>Higher-power expt. for other objects?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://doi.org/10.1016/j.neuroimage.2022.119207">NeuroImage 2022</a>
            <a class="btn" href="https://doi.org/10.17605/OSF.IO/HJ5VC">Code + Data</a>
            <a class="btn" href="https://twitter.com/martisamuser/status/1516689822374854658?s=20&t=y4kGCWUn68jnxha1U0ZqUA">X Thread</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Attentional modulation in NNs</p>
          <div class="ptitle">The function of early task-based modulations in object detection</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/SwitchSchem.png" alt="Early task modulations">
        <div>
          <p class="pmeta">
            With: <a href="https://scholar.google.co.in/citations?user=qVvqArkAAAAJ&hl=en&oi=ao">Giacomo Aldegheri</a>,
            <a href="https://scholar.google.nl/citations?user=sX0ZypwAAAAJ&hl=en&oi=ao">Marcel van Gerven</a>,
            <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            Early bias/gain modulation alleviates later capacity limits; optimized modulations look like tapping a superposition of networks rather than classic feature-similarity gain. 
            <!-- <i>Capacity of ventral stream?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="{{ site.baseurl }}/ccn18/">CCN 2018</a>
            <a class="btn primary" href="https://arxiv.org/abs/1907.12309">CCN 2019</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Scene context</p>
          <div class="ptitle">The influence of scene information on object processing</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/sc-obj.png" alt="Scene influences on object processing">
        <div>
          <p class="pmeta">
            With: <a href="https://www.linkedin.com/in/ilzethoonen/">Ilze Thoonen</a>,
            <a href="https://www.semanticscholar.org/author/Sjoerd-W.-Meijer/2061386172">Sjoerd Meijer</a>,
            <a href="https://scholar.google.nl/citations?user=IX0uaEQAAAAJ&hl=en&oi=ao">Marius Peelen</a>
          </p>
          <p class="pdesc">
            Scene co-variation biases categorization, but across 4 experiments we found no evidence that task-irrelevant scenes boost sensitivity for detecting co-varying objects. 
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://doi.org/10.6084/m9.figshare.9804725.v2">Summary slides</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</details>


<details class="projgroup">
  <summary>
    <span>Engineering computational systems</span>
    <span class="projmeta">tools, controllers, and ML systems</span>
  </summary>

  <div class="projlist">

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">Brain ↔ language interface</p>
          <div class="ptitle">Brain reading with a Transformer</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/cortext.png" alt="Cortext">
        <div>
          <p class="pmeta">
            With: <a href="https://www.linkedin.com/in/victoria-bosch/?originalSubdomain=nl"><b><u>Victoria Bosch</u></b></a>, <a href="https://scholar.google.com/citations?user=YPdEhboAAAAJ&hl=en&oi=ao">Daniel Anthes</a>, <a href="https://scholar.google.ch/citations?user=YA6DPIcAAAAJ&hl=en">Adrien Doerig</a>, <a href="https://scholar.google.com/citations?user=Ieubd0EAAAAJ&hl=en&oi=ao">Peter Konig</a>, <a href="https://scholar.google.com/citations?user=JXcWFkgAAAAJ&hl=en">Tim Kietzmann</a>
          </p>
          <p class="pdesc">
            fMRI responses to natural scenes condition word generation in a Transformer, enabling flexible readout of semantic properties like object class and numerosity.
          </p>
          <div class="plinks">
            <span class="btn primary btn-disabled" aria-label="Ongoing">Ongoing</span>
            <a class="btn primary" href="https://arxiv.org/abs/2509.23941">Preprint</a>
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">NLP / graph search</p>
          <div class="ptitle">Reverse dictionary using a word-definition based graph search</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/revmap.png" alt="Reverse dictionary">
        <div>
          <p class="pmeta">
            With: <a href="https://www.linkedin.com/in/vardos/">Varad Choudhari</a>
          </p>
          <p class="pdesc">
            Reverse dictionary via n-hop reverse search on a definition graph. Matched then-SOTA on ~3k lexicon; didn't scale well to ~80k. 
            <!-- <i>ANN-like non-linear mixing essential?</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="https://arxiv.org/abs/1606.00025">COLING 2016</a>
            <!-- <a class="btn" href="{{ site.baseurl }}/2016/11/06/reverse-dictionary">Post</a> -->
          </div>
        </div>
      </div>
    </div>

    <div class="pcard">
      <div class="phead">
        <div>
          <p class="pkicker">SNN control</p>
          <div class="ptitle">A Spiking Neural Network as a Quadcopter Flight Controller</div>
        </div>
      </div>

      <div class="pbody">
        <img class="pthumb" src="{{ site.baseurl }}/assets/btp.png" alt="Quadcopter SNN">
        <div>
          <p class="pmeta">
            With: <a href="https://in.linkedin.com/in/sukanya-patil-b45009107">Sukanya Patil</a>,
            <a href="https://scholar.google.com/citations?user=QDEeC8EAAAAJ&hl=en">Bipin Rajendran</a>
          </p>
          <p class="pdesc">
            Engineered SNN modules for polynomial transformations on spike trains. Temporal lag hinders SNN-translation of symbolic forward model for velocity–waypoint navigation. 
            <!-- <i>Need metastable SNNs.</i> -->
          </p>
          <div class="plinks">
            <a class="btn primary" href="{{ site.baseurl }}/assets/15_ijcnn.pdf">IJCNN 2015</a>
            <a class="btn" href="https://dx.doi.org/10.6084/m9.figshare.1582657.v1">B.Tech thesis</a>
            <!-- <a class="btn" href="{{ site.baseurl }}/2016/06/05/quadcopter-control-using-snn">Post</a> -->
          </div>
        </div>
      </div>
    </div>

  </div>
</details>
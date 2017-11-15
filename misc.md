---
layout: page
title: Misc.
---


<p class="message">
  Some useful resources on the internet...
</p>

- [Installing LaTeX and TexMaker on a Mac](https://thetechsolo.wordpress.com/2016/01/28/latex-on-mac-the-easy-way/)
  - The [Homebrew](https://brew.sh) and [Homebrew Cask](https://caskroom.github.io) installation instructions are updated on their respective webpages.
  - The other instructions work fine (04/10/17)
  
- [Running Tensorboard through a remote server](https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server)
  - The first solution works wonderfully (14/12/17)
  - The [Tensorboard tutorial](https://www.tensorflow.org/get_started/summaries_and_tensorboard) is pretty understandable. Basically, create summaries, initialise FileWriters with directories, and write the summaries during training.
  - If you get the error "locale.Error: unsupported locale setting", while attempting to run Tensorboard, the first solution mentioned [here](https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting) would help.
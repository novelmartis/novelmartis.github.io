---
layout: page
title: Misc.
---
<p class="message">
  Some of my informative Twitter threads.
</p>

- [Language in Interaction Symposium 2019 summary](https://twitter.com/martisamuser/status/1115679784942673922?s=20)

- [Perception Day 2018 summary](https://twitter.com/martisamuser/status/1071357743318077441?s=20)

- [Conference on Cognitive Computational Neuroscience 2018 summary](https://twitter.com/martisamuser/status/1037930887592206336?s=20)
  - Correction to the first tweet - the accepted papers can be found [here](https://ccneuro.org/2018/Papers/AcceptedPapers.asp)

<p class="message">
  Some useful resources on the internet.
</p>

- [Installing LaTeX and TexMaker on a Mac](https://thetechsolo.wordpress.com/2016/01/28/latex-on-mac-the-easy-way/)
  - The [Homebrew](https://brew.sh) and [Homebrew Cask](https://caskroom.github.io) installation instructions are updated on their respective webpages.
  - In the installation codes just drop "cask"
  - The other instructions work fine (25/08/21)

- [Running Tensorboard through a remote server](https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server)
  - The first solution works wonderfully (14/12/17)
  - The [Tensorboard tutorial](https://www.tensorflow.org/get_started/summaries_and_tensorboard) is pretty understandable. Basically, create summaries, initialise FileWriters with directories, and write the summaries during training.
  - If you get the error "locale.Error: unsupported locale setting", while attempting to run Tensorboard, the first solution mentioned [here](https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting) would help.
  - If you get the error "Tried to connect to port 6006, but address is in use", you can either try to [kill](https://www.digitalocean.com/community/tutorials/how-to-use-ps-kill-and-nice-to-manage-processes-in-linux) Tensorboard or you can switch to another port (say 8008), by doing something like "ssh -L 16006:127.0.0.1:8008 xx@xxxx" and access tensorboard on your local machine at "127.0.0.1:16006/"

- [Installing Jekyll for creating a website](https://x-team.com/blog/build-a-free-website-with-jekyll-and-github-pages/)
	- If your website is configured to an older version of Jekyll, you might not use the bundler and use 'jekyll serve' alone. In that case, refer to [this issue](https://github.com/Huxpro/huxpro.github.io/issues/62). After that, manually install all the packages jekyll says are missing by using 'gem install jekyll-x', where x is the package of interest (e.g. archives)
  - If you want to make a page other than the Blog your homepage, check [this discussion](https://github.com/jekyll/jekyll-help/issues/289).
  - If you are having trouble with ruby or jekyll (if "jekyll -v" throws an error), you might want to perform a clean install of homebrew to jekyll. You can do so with [this script](https://github.com/monfresh/laptop)

<hr>

This webpage, hosted with [Github Pages](https://pages.github.com), was built with [Jekyll](http://jekyllrb.com) using the [Hyde](https://github.com/poole/hyde) theme designed by [@mdo](https://twitter.com/mdo). The image of [Goku riding Nimbus](https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-241742.png) was taken from [Taringa!](https://www.taringa.net/post/imagenes/18835146/Wallpapers-Dragon-Ball.html)

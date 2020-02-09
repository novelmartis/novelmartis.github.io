---
layout: post
title: Threshold-free cluster enhancement (TFCE) in CoSMoMVPA
tags: [2020, coding, fmri]
description: Details about the implementation of TFCE in the MATLAB toolbox CoSMoMVPA used for multi-variate pattern analysis in neuroimaging.
comments: true
---

While the [2016 Frontiers paper][16cosmo] introduces the framework of CoSMoMVPA, the exact details of how it implements threshold-free cluster enhancement (TFCE) for multiple-comparisons correction are somewhat opaque. This blog post is aimed at describing those details.

#### The principle

As I understand it, using [TFCE][09tfce] we perform voxel-level inference about the existence of an effect while accounting for the "support" of neighbouring voxels towards the existence of that effect at the given voxel. If the given voxel is a part of a "hill" on a variable's landscape, both the extent of that hill and the value of the variable at the given voxel contribute towards the inference about that value being higher than baseline.

There are two steps in this procedure:
1. Computing a new variable, the TFCE value, which quantifies the amount of "support" a voxel has - exemplified in the image below (Fig 1. from the [TFCE paper][09tfce]).
2. Computing the null distribution of TFCE values at every voxel, then computing z-scores on these distributions for the values computed in step 1, which can then be thresholded for each voxel at a desired false discovery rate for statistical inference.

![TFCE computation]({{site:url}}/assets/tfce-compute.png)

#### Computing the TFCE value

$$TFCE(p) = \int_{h_0}^{h_p}e(h)^Eh^Hdh$$

While the above formula defines TFCE, in CoSMoMVPA it is computed in an iterative procedure as follows. 

Let's say the maximum value of the relevant variable (e.g. GLM weights in fMRI) across voxels is $$h_m$$. Then we define $$\approx (h_m-h_0)/\Delta h$$ markers between $$h_0$$ and $$h_m$$, where $$h_0$$ is the baseline value. At every marker, we list the voxels with values above the value of the marker. We then identify the largest possible clusters with contiguous voxels. In each cluster, every voxel's TFCE value is incremented by $$\Delta h(\text{# of voxels in the cluster})^E(\text{value of the marker})^H$$, where usually $$\Delta h = 0.1$$, $$E = 0.5$$, and $$H = 2$$ (check out the [TFCE paper][09tfce] for justification).

This computation of TFCE values is done with the function [<i>cosmo_measure_clusters</i>][cmc] in CoSMoMVPA.

This procedure is repeated after flipping the variable values around the baseline value, to quantify the TFCE values for any voxels with values below the baseline. Two sets of TFCE values are returned (each voxel is positive either in one or none of the maps) which are then compared against the null distribution as explained in the next section.

In a typical neuroimaging analysis, we have values for a given variable across voxels of the aligned brains of N participants (e.g. in MNI space). The TFCE values are computed across the voxels over a measure of the standardized mean across participants. Precisely, for each voxel, after subtracting the baseline value, the mean across participants is divided by the standard error, which is then transformed with the Student's-T cumulative distribution function (CDF), which is finally transformed to a z-score with the inverse normal CDF. This is the variable over which TFCE values are calculated.

#### The null distribution and statistical inference

As we are usually interested in inferring if the voxel's value is above/below baseline, the null distribution of voxel responses would be equally spread around the baseline. In CoSMoMVPA, this is accomplished by iteratively flipping the sign of the voxel values of a random half of the participants (after subtracting the baseline value). For each iteration, the TFCE values are computed, separately for the positively and negatively valued voxels, as above, to generate null distributions of TFCE values for both the positively and negatively valued voxels respectively. 

In the case of the positively valued voxels, the number of iterations where the TFCE values for the positively valued voxels, in those iterations, were less than the actual TFCE value is computed. If that number is more than half of the total number of iterations, that number is scaled to lie between 0.5 and 1 (1 where all iterations yield lower TFCE values than the real one). Similarly, for the negatively valued voxels, that number is scaled to lie between 0 (0 where all iterations yield lower TFCE values than the real one) and 0.5. Then using the inverse normal CDF, a z-score is computed for each voxel which is the output of the entire procedure.

If we wish to restrict the false discovery rate to, say, 5%, we can threshold the final output at $$z\geq1.96$$ and $$z\leq-1.96$$.

#### Example script

Adapted from [CoSMoMVPA demo code][dst].

```Matlab
% Let's say ds contains the voxel values (e.g. output of a searchlight analysis) across the aligned brains of N participants.

% Compute voxel neighborhoods (useful in clustering required during TFCE computation)
cluster_nbrhood = cosmo_cluster_neighborhood(ds);

% Parameters of the procedure
opt = struct();
opt.niter = 10000; % generate the null distribution with 10000 iterations
opt.h0_mean = 0; % baseline value
opt.null = [];

% Compute the TFCE values (cosmo_measure_clusters is called within this function) and output the z-scores
tfce_zscores = cosmo_montecarlo_cluster_stat(ds,cluster_nbrhood,opt);

% Compute z-threshold for statistical inference
p = 0.05;
z_th = norminv(1-p/2); % two-sided test

% Create thresholded maps and save them
pos_voxs = tfce_zscores.samples >= z_th;
neg_voxs = tfce_zscores.samples <= -z_th;
tfce_zscores.samples = pos_voxs;
cosmo_map2fmri(tfce_zscores, 'pos_voxs.nii');
tfce_zscores.samples = neg_voxs;
cosmo_map2fmri(tfce_zscores, 'neg_voxs.nii');
```



[16cosmo]: https://doi.org/10.3389/fninf.2016.00027
[09tfce]: https://doi.org/10.1016/j.neuroimage.2008.03.061
[cmc]: http://cosmomvpa.org/matlab/cosmo_measure_clusters.html
[dst]: http://www.cosmomvpa.org/matlab/demo_surface_tfce.html



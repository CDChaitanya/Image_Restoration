# Image Restoration

## Implementation Result
### Input
<div align="center">
  <img align="center" src="Image Restoration/abraham.jpg" height="400" width="300">
  <img align="center" src="Image Restoration/mask.jpg" height="400" width="300">
</div>

### Intermediate Output
<div align="center">
  <img align="center" src="Image Restoration/Output/output_3.png" height="400" width="300">
  <img align="center" src="Image Restoration/Output/output_4.png" height="400" width="300">
</div>

### Final Output
<div align="center">
  <img align="center" src="Image Restoration/Output/final_output.png" height="400" width="300">
</div>

### Motivation
- In our day-to-day life, we come across lots of images. But these
images may have some issues like the image may be a blur, the image is noisy
or there may be some superimposed data on the image like date place or any
kind of text. This was about the digital images but if you’re having an old
photograph which is deteriorated due to a period of time, so all such images
have lost their data information and we want that data so what is the solution
for this answer is image restoration.
- With image restoration, we’ll be able to restore the degraded part
of an image. Basically from a very long back inpainting techniques are there
for restoring old sculpture, monument, or any important thing. So the
technique is the same as used by professional restorers. There is another case
when the image is perfect but there is an unwanted object in that image and
we don’t want that so in such cases also inpainting can be used.
- Thus with the help of the inpainting technique, we can retrieve
the data of damaged images also we can remove unwanted objects from the
image. This technique resolves lots of problems about degraded images or
damaged images so this is a much-needed technique.

### Fundamental Concepts
- <b>Image Restoration:</b> Restoration is a process that attempts to reconstruct or
recover an image that has been degraded by using a priori knowledge of the
degradation phenomenon.
- <b>Image Inpainting:</b> The process of filling-in missing data in a designated
region of the visual input. The objective of the process is to reconstruct
missing parts or damaged image in such a way that the inpainted region
cannot be detected by a causal observer.

Nowadays, there are different approaches to image inpainting are available.
And we can classify them into several categories as follows:-
1) Texture Synthesis based Image Inpainting.
2) PDE based Image Inpainting.
3) Exemplar based Image Inpainting.
4) Hybrid Image Inpainting.

## Texture Synthesis Based Inpainting
- Texture synthesis is one of the earliest techniques of image Inpainting.
And this technique is used to complete the missing regions using similar
neighbourhoods of the damaged pixels.
- These synthesis based techniques perform well only for a select set of
images where completing the whole region with homogenous texture
information.
- The main objective of texture synthesis based inpainting is to generate
texture patterns, which is similar to a given sample pattern, in such a
way that the reproduced texture retains the statistical properties of its
root-texture. And it does not appear simply as a tiled rearrangement of
the root-texture.
- Texture synthesis approaches can be categorized into 3 categories:
Statistical, pixel-based and patch-based.
- Statistical methods are more likely to succeed in reproducing irregular
textures, but usually fail to reproduce structured/regular textures.
- On the other hand, pixel-based methods build on the sample texture
pixel-by-pixel, and their final outputs are of better quality than those of
statistical methods, but they usually fail to grow large structured textures.
- Finally, patch-based methods build on a sample texture patch-by-patch as
opposed to pixel-by-pixel, thus they yield faster and more plausible
regular textures.
- So I can say that there is no universal texture synthesizer is present.
- These algorithms have difficulty in handling natural images as they are
composed of structures in form of edges.
- In some cases, they also require the user to specify what texture to
replace and the place to be replaced.
- It is important to understand that these methods address only a small
subset of Inpainting issues and these methods are not suitable for a wide
variety of applications.

<div align="center">
  <img align="center" src="Image Restoration/Output/ts.png" height="" width="">
</div>

## PDE Based Image Inpainting
- Partial Differential Equation (PDE) based technique is proposed by Bertalmio et.al.
- This technique is the iterative technique. The main idea behind this technique is
to continue geometric and photometric information that arrives at the border of
the occluded area into area itself.
- This is done by propagating the information in the direction of minimal change
using “isophote lines”(lines with equal gray-scale value). This algorithm will
produce good results if missed regions are small one.
- But when the missed regions are large this algorithm will take so long time and it
will not produce good results.
There are two main models in Image Inpainting based on PDE those are as
follows :-
1. Total Variational Model (TV Model)
2. Curvature Driven Diffusion Model (CDD Model)

- The TV model uses anisotropic diffusion (redusing image noise without removing
significant parts of image) based on the strength of the isophotes.
- This model performs reasonably well for small regions and noise removal
applications. But the drawback of this method is that this method neither
connects broken edges nor greats texture patterns.
- The TV model then extended to CDD (Curvature Driven Diffusion) model. In
which it included the curvature information of the isophotes to handle the
curved structures in a better manner.
- Then telea propose a fast marching method. This is considered as a PDE method
which is faster and simpler to implement than other PDE based algorithms.
- All of the above mentioned algorithms are very time consuming and have some
problems with the damaged regions with a large size. PDE based technique has
been widely used in number of applications such as image segmentation,
restoration etc.
- These algorithms were focused on maintaining the structure of the Inpainting
area. And hence these algorithms produce blurred resulting image. Another
drawback of these algorithms is that the large textured regions are not well
reproduced.

<div align="center">
  <img align="center" src="Image Restoration/Output/pde.jpeg" height="" width="">
</div>

## Exemplar Based Image Inpainting
- This yet another important and effective Inpainting technique. The exemplar-based
technique is comprised of two simple steps:
1) Prioritization has been completed, and
2) The best matching patch has been chosen.

- We’ll fill the missed area with samples from known matching patches, whose
similarity is calculated by some metrics, using the exemplar-based methodology.
- The exemplar technique helps in selecting the most preferable matching patch
from the source region and the filling is done on the basis of priority, Once the
priorities of the pixels have indeed been computed, the pixel with the topmost
value is picked as the target pixel to rebuild and the affected section in a pixel - by-
pixel manner.
- For a natural looking result, the edges should be continued which means that the
patch that contains high structural information should be filled first. With this
principle, patch priority P is introduced patch priority is defined as

<div align="center">
  <img align="center" src="Image Restoration/Output/ex_p.png" height="" width="">
</div>

<p align="center"> <b>P (p) = C (p). D (p) </b></p>

- The confident term C (p) and data term D (p) is defined as,
- Where |Ψp| is the area of Ψp, np is the normal vector of the front δΩ, is the isophote at p and α is the normalizing
factor which equals 255 for 8-bit grey-scale image.
- The confident term C shows the ratio of known pixels surrounding at the center of target patch.
- The data term D shows the strength of the edge at the target patch.
- The process of Exemplar-based approach can be detailed as follows. Firstly, the confident term is initialized by assigning to C (p) =0 for all p belongs to Ω (target region) and C(p) =1 for all p belongs to U\Ω (source region)

<div align="center">
  <img align="center" src="Image Restoration/Output/exemplar.png" height="" width="">
</div>

## Hybrid Image Inpainting
- The texture synthesis-based technique is the best fit for the texture part
but not so good with the structure whereas the PDE-based technique is the
best fit for the structure part not good with the texture part. So both
techniques are combined and this technique is called the hybrid technique.
- When we use the hybrid technique for restoring the damaged part the
texture technique will take care of texture and the PDE will take care of the
structure.
- The hybrid inpainting technique can also be referred as Image Completion.
It is the best to fit for filling large target regions. This technique preserves
both textural and structural quality.
- This technique converts the image into two parts one part is homogenous
for the texture region and another one is non-homogenous for structural
regions.
- When it comes to filling wider areas, these algorithms are very
computationally costly. The hybrid technique works in two steps: the first is
structure reconstruction, and the second is texture synthesis.

<div align="center">
  <img align="center" src="Image Restoration/Output/hybrid.png" height="" width="">
</div>

## Comparsion
 
<div align="center">
  <img align="center" src="Image Restoration/Output/comparsion.png" height="" width="">
</div>

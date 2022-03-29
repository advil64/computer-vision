### Segmentation
- Theres multiple ways to do segmentation but what is it in the first place
- Mid-level vision is the first way I guess
- Figure ground segmentation is basically determining what is the foreground and background of a given image
- It's an ambiguous problem
- Gestalt is german for a group, basically how do people tend to group items in pictures
- Humans tend to subconsciously make groupings for certain things in their heads
- Segmentation can be multiple things like color, or orientation or something
- Paralellism, symmetry, continuity, and closure are all cues for segmentation and how we group things together
- Occlusion too is also a very good cue
- So how do the computers figure this shit out? It seems very subjective
- Segmentation, Grouping, Perceptual Organization, and fitting are all related terms, just used by different people in different fields
- You have to collect things called tokens and then associate a bunch of these tokens together with some kind of algorithm/model

### Image Segmentation as Clustering
- Recent progress has been made in semantic segmentation in deep learning to label every pixel as a class and thus a region.
- Hierarchical clustering is a very old algorithm in the field, you take a bunch of points and build a tree of the distance from each other points
- It's a very simple straightforward type of clustering in segmentation
- The watershed algorithm is like filling water from a low gradient up to the high gradient and thus finds regions by doing so
- It tends to oversegment the image into what's called superpixels 
- K-Means is another option for clustering pixels into segments
- Graph based image segmentation looks at the connectivity between different pixels and also weight between them to figure out groups
- The weights in image segmentation measures similarities called affinity
- To measure affinity between different pixels you can use things like intensity, distance, color and so on
- You can do image segmenting with the graph approach by doing graph cuts algorithm, basically how can you seperate a graph into K different ones for the cheapest way
- Spectral clustering I kind of zoned out for this part but for sure google it
- Something about eigenvalues or some shit refer to the textbook for more info
- Shi and Malik (2000) suggest a normalized cut: cut the graph into two connected components such that the cost of the cut is a small fraction of the total affinity within each group.

### Deep learning segmentation
- And then we go over segmentation using deep learning
- Basically you apply convolutions to a certain point for an image and then do a bunch of 1x1 convolutions [stuff](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578)
- Look into Up Convolution, also look into fully convolutional networks for semantic segmentation
- Encoder/decoder architectures can also be used to learn the segmentation of an image
- Look up the segnet paper to learn more abou this stuff
- what the heck is upscaling and down scaling?
- He literally just opened a bunch of papers and went over them at this point
- 
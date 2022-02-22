### Contour Finding
- When you first find a contour you can trace it
- Chain codes basically you trace the contour and encode something?
- If an object translates to another location, its chain code does not change
- If it rotates, its chain code will def be different it is not rotation invariant
- Chain code is not scale invariant
- Absolute vs Differential chain code differential chain code can be rotation invariant in some cases
- You can find the perimiter of the object using the chain code. You basically sum the chain codes and apply a correction value
- You can also measure the roundness of an object with chain codes, measure the area and divide it my the perimiter squared which is a measure of circularity
- You can also find the bounding box of a region which is the box within which you have an object
- A convex hull is the smallest polygon within which all of the points fit
- You can also measure the convexity of an object which is the ratio between the length of the convex hill and perimited of region
- Density is the ratio between the area of the region and area of the convex hull
- Centroid in the x dimension is the sum in the x cordinate divided by the number of pixels in the region (center of mass of the object)

### Moments
- Moment of order 0,0 is the area of the region or the cardinality of the set
- Moment of order 0,1 is the sum of u cordinates
- Moment of order 1,0 is the sum of v cordinates
- Central moments are position independent which shift the coordinate system to the centroid
- To get a central moment you just subtract the u and v by the initial centroid
- Normalized central moments are invariant to the size of the region
- You can ge the geometric properties of moments such as direction of the major axis and eccentricity which is a measure of how thick/thin the object is
- Hu moments are seven combinations of the normalized central moments
- They are invariant to translation, scaling, and orientation

### Projection
- For every row you count how many foreground pixels there are, it's basically a histogram
- De-Skewing images is a piece of cake with this technique. You basically try to rotate until you get the desired histogram view


There are however shortcomings of these types of simple vision systems, alot of the reasons are because of the fact that our world is in 3D

## We're going into 3D!
  
### Point operations
- Map pixel values without changing size, geometry, or local image structure
- Basically you have some function and apply to each pixel, for example you can modify the brightness of an image and a bunch of other shit
- Photo contrast function is point operations, contrast is basically you take a gray scale image and take a histogram. Contrast is the range of the histogram which means the pixels are nice and contrasting.
- Autocontrast basically stretches the pixel histogram to create more contrast
- Histogram equalization is adjusting images in a way that their resulting intensity distributions are similar
- Intesity something something equalize something
- You can basically force an image to conform to a particular intensity distribution for each image and use point operations to make it so
- what the fuck is intensity
- You can't do things like blur an image with point operations

### Filters
- A filter is a function that is applied over a neighborhood of pixels
- A linear filter is a weighted average filter 
- A filter over an image is complex because it requires nested loops
- If your filter is outside the image, you should force the filter within or just pad the image
- $I' = I * H$
- If you apply a filter with only one pixel that is on, the center value of the filter will show up at that single location
- A whole bunch about convolutions that I was not paying attention to
- Seperability
- A gaussian filter is the gaussian function in 2D which is used to blur images
- smoothing images is useful to reduce noise
- If a filter is seperable this means you can break it down into vectors which cuts down computing power needed

### Noise
- Gaussian filter allows noise values that could be greater than the maximum camera output or less than zero
- Noise may not only be because of a certain filter as there could have been defects in the camera
- What is the noise image?
- Find a filter with the sum of the squares is les than one
- Paralell weights and window means that they are the same?
- normalized correlation? something cosine something something
- Center surrounding cells
- Something something maximum response something
- 
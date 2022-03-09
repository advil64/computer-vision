### Texture

- Texture is an organized patterns of regular sub elements, and we have to find ways to represent these patterns
- Recovering 3d objects from 2d objects is called recovering shape from texture, you can recover things like depth from this process
- Recovering materials from textures is incredibly important, denim from the stitch for example
- Texture is an element that repeats itself?
- Textone is an element that repeats itself, texture is a bunch of textones
- Our goal is to find a computational method that basically models these textures
- Textone theory was developed by a crazy cool rutgers prof
- Co occurance matrix is a matrix that you basically look at that configuration and tally the number of times that pattern co occurs in that specific configurations
- You can extract certain aggregation metrics from the co occurance matrices like entropy and shit
- Bad thing about this is computationally expensive
- Also you have a shit ton of different patterns

### Textures with filters
- You can look for textures using filters as well
- Spots and bars are probably the most common types of patterns you see when you apply a texture filter
- Same type of filters that we saw before
- There are certain filter banks that you can use to detect textures
- What is the scale of the filter? Certain scales work better for certain textures
- Texture representation is basically pooling from the result of the filters into a big vector which is useful for classification
- You have to do rectification which is applying the filter and seperate into two different maps one which has a negative/positive value. 
- What is a positive and negative response? what's the difference?
- Positive and negative responses depends on the background and foregrounds dark vs light

### How many
- SO like how many filters should you use?
- Theres are tradeoff between the number of filters and detailed output but also redundant output

### Process
- Once you get the vectorized filter responses, you can do kmeans and then get the 3d tectones
- the k means part is useful to generate a codebook of textones
- Bag of words textures

### Gabor Filters
- Fourier transform for an image results in the power spectrum of the whole image which captures frequencies all over the image
- Not useful in textures tho cause there are local textures
- Basically we need to do fourier transforms locally in the image
- Multiply the cosine waves by the gaussian function, this will make the cosine function localized which then you can move around to figure out the different textures in the image
- Gabor filter banks are localized fourier transfors?
- You also get rotation invariant gabor filters which look like concentric circles no joke

### Scales
- Might have to search over scales cause you dont know how big the object is in the particular image
- Image pyramids have a problem with aliasing, if you subsample high frequencies, you loose the high frequency with aliasing
- Guassian pyramid is useful to solve the problem, it does anti aliasing
- Each layer you smooth with the gaussian before you subsample it
- You just keep doing that shit until you get the finally subsampled image
- You basically get rid of the high frequencies at that point
- You basically take out one sample from each set of pixels which is called subsampling

### Laplacian Pyramid
- Useful to solve the redundency problem
- You're subtracting the layers of the gaussian pyramid which is only keeping the lost information
- Basically when you keep the differences, the very top level will only keep its own level frequencies or the frequencies that are lost basically
- You keep hella bands
- You can also use the laplacian pyramid to reverse engineer the orignal image
- Oriented pyramids, you're gonna build the laplacian pyramid and gather the oriented edges, they're basically a circle on three sides with a right angle inside kinda like a 270 degree C
- After you build your pyramid, you have to apply your filter bank to every layer in the pyramid

### Filter Response
- Basically you do a filter response for each location with the filter and then create a codebook and do k means

### Random
- Gabor filters basically keep getting smaller to gather more minute information, ppl typically use 48 Gabor filters

### Local Binary Patterns
- Remember before how we wanted to figure out the diff patterns? we basically can convert the pattern to a binary number which is illumination invariant
- Basically you keep rotating the binary code and then find the minimum which makes this information rotation invariant

### texture classification using CNNs
- Basically remove the classifier layer and take the response of the last layer to inform textures of your image classes
- You can also take the pre trained model and finetune it to get the texture of the classes

### Texture Synthesis
- A problem where I get an image/area of a texture and want to generate bigger images that contain that texture which looks natural
- Basically you have a small imageof a texture and search a bunch of images for the same texture and then fill in your new synthesized image with the example image
- The window of the image matching matters, too big means it'll basically be replicate but too small means it becomes too random
- This stuff is also related to image fill in
- You can also just extend an image by doing this, making bigger

### Texture mapping using CNNs
- Look into From Bow to CNN 

### Color Perception
- Every light source has a different color distribution
- Every wavelength is the combination of the illumination and reflectance which comes to the eye/camera where the cones/sensors absorb that shit
- They absorb a certain amount of wavelengths
- This whole thing is like a bunch of integrations
- RGB color cube is an additive color system, add primary colored light to perform different colors
- RGB might not be that intuitive? Bro what?
- There's other color spaces that might seem more intuitive
- Three important concept  are Hue, Saturation, and Luminance which is how much light is in each pixel
- You can get luminance value from Y from RGB
- Desaturating color images is basically subtracting certain pictures RGB values until you get it to a gray scale image
- Google the HSV and HSB color spaces which stand for Hue, Saturation, and brightness
- This shit looks like the opposite of RGB


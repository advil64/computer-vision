## Lecture 2

### Rods & Cones
- There are certain types of photoreceptor in your eyes that are typically suited for a certain light levels
- Rods are high sensitivity which is useful in low light but are low resolution and there are 100 mil of them
- Cones are sensitive to higher levels and have a higher resolution there are 5 mil of them
- Cones also have different sensitivity to light, L M and S cones have different sensitivity to Violet, Green, and Blue
- Fovea is the highest concentration of photo receptors, it does not have any rods and creates very high resolution images
- There's a blind spot in the area that the optic nerve attaches to the eye

### Ganglion Cells
- Do the first processing in the eyes
- Have a center surrounding structure, on center cells will fire when the light is in the center and vice versa
- Ganglion cells are very good at edge detection and they don't really acre about the brightness as much as the edges which is what is important for recognizing objects more than the color or brightness
- If you have a signal and look at the distribution of values, if you take the differences of the values an look at the distribution at differences, you'll find that the distribution is very close to zero whereas it might be very wide otherwise?
- The ganglion cells look for edges by looking at differences in color? More in depth understanding needed?
  
### M vs P Cells
- There are two kinds of ganglion cells, M and P
- P cells have greater temporal vs M which has greater spatial resolution
- Spatial frequency refers to the number of straight lines which are close together, basically very sharp edges. Think sine waves which have a low spatial frequency
- Temporal frequency is ask to clarify is this a light like blue vs red or edges?
- M cells have a larger conversion of photoreceptor vs P which does not
- This mean M cells has a better light sensitivity
- Get a better understanding between M and P cells, I have no idea what he's saying
- M cells are larger and faster nerve conductivity which means that they can capture quick changes in light and transfers to brain quickly
- P cares more about high resolution images with non flashing light or just calmer waves
- M cells are better for motion and perception
- P cells are better for color, texture and patterns

### LGN
- Bundle of axons leaving the eye
- Not really sure the use for it? 
- M and P cells send their signals to the LGN which then feeds the signal to the brain

### Primary Visual Cortex
- Made up of center-surrounding cells, simple cells, and complex cells. These three building blocks inspired the CNN
- Center-surrounding cells have the two types of layers, on center and off center layers. They are used depending on the type of input. If the light is straight in center then these cells are used
- Siple cells are fired when an object is in certain location and  detect edges at a location and the orientation of the image.
- There are different simple cells for certain orientations
- Center surrounding -> simple -> complex is the feed forward process
- Cells responses become very specific and specialized at the start
- They also become more general as you get deeper in the brain and they basically put the pieces together
- Go over the specific vs general stuff, not sure which is which
- Different cells fire for different orientation of lines and different eyes, There's a shitton of cells which all have different jobs (simple cells)
- Neurons that fire together are wired together (Hebb Rule). Meaning if they fire for the same condition that means they are also wired usually your brain creates inherent structures.

### CNNs
- CNNs work by first taking in an input then a bunch of layers of feed forward cells which are made up of convolutional layers and sampling layers
- Convolution layers are multiple feature maps which apply certain convolutions on an area of an image and looks for a specific pattern in an image. Each layer is trained to detect the orientation of a specific part of the image
- convolutions layers are encoded by the location of the edges and detect depending on orientation
- Subsuming layers aggregated the firing from the convolutional layers and averages/pools the firing from a bunch of convolutional cells and does some type of aggregate operation on it
- Then the next convolution layer again detects a certain pattern but this time it combines multiple edges of different orientations which detectsa more specific pattern and a larger number of patterns
- The network is able to learn different types of data based on the type of inputs provided/data trained on

### Limitations of humans
- humans can't see certain wavelengths such as infared waves
- they have a blindspot

### Pinhole cameras
- google it
- Smaller pinhole causes more diffraction which means unclear image
- Bigger pinhole causes too much light
- distant objects are smaller in pinhole cameras (compared to the distance between the light and camera?)
- Pinhole cameras don't have enough light enter which means that they are dark and not good for reconstructing images

### Lenses
- Snell's law basically all of the E&M stuff coming back to haunt me
- A lens is many small prisms combined to that a light from a single point comes back to a single point. Lens can only focus if you put the film in the right location
- Each lens has a focal point
- Thin lenses have a right focal point and left focal point. If the ray is paralell, it has to go to the right focal point and vice versa

### Random Stuff
- Can't reconstruct 3d image from a 2d one unless you have certain constraints
- 
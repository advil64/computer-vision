## Cameras and Lenses

### Pinhole Cameras
- y = f * Y/Z
- Google how pinhole cameras work
- You can represent images from pinhole cameras as a matrix
- Further objects from the pinhole tend to be smaller while vice versa
- Focal point changes make an image more/less magnified

### Lenses
- Lenses collect more light than pinhole cameras which makes brighter images
- Snell's law look it up
- ![snell's law](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Snells_law2.svg/1200px-Snells_law2.svg.png)
- ![thin lens](https://phys.libretexts.org/@api/deki/files/5056/CNX_UPhysics_35_04_Thinlens.jpg?revision=1)
- Focus changes on where the object is in relation to the thin lens
- Thin lens equation can tell you how far from the lens will give you the image in most focus
- $\frac{1}{Z} + 1/z = 1/f$ where the distance between the lens and the object is Z and lens to the image place is z then you get f which is the focal point.

### Depth of field
- In a thin lens, there is only one plane in focus, this is a problem. In real lenses, the system is designed to have a range of values in focus [Z1, Z2].
- In an eye, the muscles next to the eye lens make the lens thinner or thicker

### General Lenses
- $f$ is proportional to the radius of the lens, a thick lens has a closer focal point than a thin lens which has a focal point which is farther away. Thin lenses bend the rays less than a thicker lens. The power of a lens to bend the rays is called optical power
- Accommodation of the eye refers to the act of physiologically adjusting crystalline lens elements to alter the refractive power and bring objects that are closer to the eye into sharp focus.
- Lenses have some imperfections like shape, refractive index, scattering, geometric aberrations, chromatic aberrations
- Geometric aberrations, one type is spherical. Basically only some rays coming from one point intersect at the center which creates a fuzzy blob rather than an actual image.
- Radial distortions are made up of barrel and pincushion distortions. Image magnification decreases with distance from the optical axis for barrel distortion. Pincushion is kind of the opposite
- Chromatic distortions are when colors get distorted and happens more on the boundaries
- Vignetting is when a bunch of rays coming from the first lens get lost on the way to another lens. This causes the image to be a bit darker in the periphery
- Go over the milestones of images/pictures first photo in 1816
- CCD and CMOS cameras were important technologies that are still used today

### Digitizing images
- To make a digital image you need to do spacial, temporal sampling and quantization of pixel values
- Digital camera does a bunch of stuff
- Camera has an aperture which controls how much light is allowed
- By opening and closing the sensor you are doing temporal sampling which is necessary for digitization
- Aperture is a hole in front of the lens which allows a certain amount of light to come through into the camera. Bigger aperture gives a shallow depth of field and smaller hole has deeper depth of field
- Shutter speed also matters, slow speed means more light whereas fast speed means less light. If you have slow shutter speed you will have more motion blur. 
- ISO is a measure of the density of the film, a denser film means you're more sensitive to the light. You will get a cleaner image with a smaller ISO
- The exposure triangle tells you how to control the three areas for the perfect image
- ![triangle](https://linespex.com/wp-content/uploads/2019/11/exposure-triangle-1030x1019.jpg)

### CCD vs CMOS
- CCD cameras acumulate signal charge in each pixel proportional to the local illumination intensity
- CMOS accumulates signal charge in each pixel proportional to the illumination intensity
- CCD has a sensor array of photoreceptors which moves each charge to voltage conversion by bouncing off the rays to their neighbor receptors and passes off until the convertor
- CMOS has a bunch of photoreceptors as well but converts each ray immidietly as each receptor also has a convertor
- CCD is somewhat better as there is only one charge to voltage conversion which gives you a less noisy image
- Check this out [CCD vs CMOS](https://www.yumpu.com/en/document/read/22064282/ccd-vs-cmos-facts-and-fiction-teledyne-dalsa)
- Fill factors are different between the two, CCD has a higher fill factor which is the fraction of pixel area that integrates coming light. collects more photons
- The chip size is important as well, bigger chip is higher resolution because it is more photo sensitive
- ADC resolution, the analog to digital conversion, more bits is better which mean more quantization

### Bayer Filter Pattern
- Green channel portrays the most information
- 3 CCD cameras are color separating cameras into 3 colors and then combine
- Google this stuff a bit more

## 2-D (flat) vision systems

### Image Segmentation
- The big problem is that pixels overlab regions both the object background and foreground leading to largely blurry images
- You can kind of fix this by thresholding which $B(u,v) = 1$ if $I(u,v) < thresh$ and vice versa.
- You can come up with the threshold by looking at the probability distributions
- Use the triangle algorithm to come up with the threshold
- ![triangle algo](https://www.researchgate.net/profile/Ian-Young-10/publication/2890160/figure/fig4/AS:341561129881607@1458445927232/The-triangle-algorithm-is-based-on-finding-the-value-of-b-that-gives-the-maximum-distance.png)
- You can also pick threshold based on the best contrast result
- You can define neighborhoods which are based on connectivity (4 vs 8 connectivity). Two disjoint sets of pixels are 4 connected if they have 4 neighbors or some shit
- Two pixels are connected if there's a path between the two of them in the fore/back ground
- Different disjoint sets translate to different objects
- Sometimes you can use opposite connectivities for an image to make sense

### Flood Fill Region Labeling
- Just a simple way to find different regions
- However things might not be perfect as noise might interfere with connectivity
- Dilation expands the connected sets to fill in holes and connect sets
- Erosion shrinks the connected sets of 1s in a binary image, it removes bridges, branches, and small protusions.
- Look up dilating and eroding, I zoned out
- Watch this video or somthin [vid](https://www.youtube.com/watch?v=uUweXBmm978)
- Look up opening and closing and whatnot
- Closing is a compound operation of dilation followed by erosion
- Opening is the compound operation of erosion followed by dilation
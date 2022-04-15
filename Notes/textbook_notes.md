### Linear Filters
- As well, the Fourier transform of two convolved images is the product of their individual Fourier transforms
- Both correlation and convolution are linear shift-invariant (LSI) operators, which obey both the superposition principle and the shift invariance principle, which means that shifting a signal commutes with applying the operator (  stands for the LSI operator).
- A convolution that can be split into a 1-D horizontal and vertical convolution which speeds up the actual convolution and requires a total of 2K operations per pixel instead of $K^2$ is called *Separable*
- To figure our whether a kernel is separable you need to take its Singular Value Decomposition and do a bit of math that I don't quite understand [Check this out](https://bartwronski.com/2020/02/03/separate-your-filters-svd-and-low-rank-approximation-of-image-filters/)
- A filter is linear if their response to a sum of two signals is the same as the sum of the individual responses
- This is equivalent to saying that each output pixel is a weighted summation of some number of input pixels
- Non-linear filtering is more edge preserving, i.e., it has less tendency to soften edges while filtering away high-frequency noise.
- In the bilateral filter, the output pixel value depends on a weighted combination of neighboring pixel values

### Fourier Transforms
- How can we analyze what a given filter does to high, medium, and low frequencies? The answer is to simply pass a sinusoid of known frequency through the filter and to observe by how much it is attenuated.
- The Fourier transform is simply a tabulation of the magnitude and phase response at each frequency, it is the response to a complex sinusoid of frequency $\omega$ passed through the filter h(x)
- [Helpful Resource](https://homepages.inf.ed.ac.uk/rbf/HIPR2/fourier.htm#:~:text=Brief%20Description,is%20the%20spatial%20domain%20equivalent.)
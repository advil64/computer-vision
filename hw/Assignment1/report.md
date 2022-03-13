### Enhancements

- Used Otsu's Method to find the optimal threshold value for both train and test images
- Used binary dilation to close gaps in letters
- 0.52, 0.328, 0.31 without k nearest neighbors and no dilation, and no otsu's method
- 0.66, 0.43, 0.36 with k nearest neighbors and with dilation, and otsu's method
- 0.52, 0.34, 0.36 without k nearest neighbors, with otsu's method, and without dilation
- 0.52, 0.34, 0.36 without k nearest neighbors, without otsu's method, and with dilation
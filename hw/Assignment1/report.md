## HW1 AC1771

The goal of this assignment was to use HU moments to recognize characters which were provided by the professor. Given some training chars we used the nearest neighbor to find the closest match. The initial results without enhancement for training, test1, and test2 are as follows: 0.52, 0.328, 0.31

### Otsu's Method

To figure out what the best binarization threshold should be, I used Otsu's method which is a widely regarded method to find the threshold for binarization. Using this method I got the following results for the accuracy of the training, test1, and test2 respectively: 0.52, 0.34, 0.36.

### Binary Closing

Next I used binary closing to close any gaps that were in the letters being read. This is simple as we learned in class. Using this method I got the following results for the accuracy of the training, test1, and test2 respectively: 0.52, 0.34, 0.36. As you can see it's basically the same the previous results

# KNN

Lastly I used the above to methods but grouped it with K-Nearest Neighbors which takes a majority of the k neighbors rather than the closest single one. That bumped up my accuracy a little bit for train and test1. Using this method I got the following results for the accuracy of the training, test1, and test2 respectively: 0.66, 0.43, 0.39.

As you can see it helps a lot in the train section but that might be because the actual point is included in the 5 nearest neighbors, however there was also a significant improvement in the two test sets as well so it might be worth considering looking into this method.

# dimensionality reduction
for i, k in enumerate(normalized.keys()):
    letter_means[k] = np.mean(normalized[k], axis=0)
combined_means = np.vstack([letter_means[k] for k in letter_means])


# print('Letter: ', i+1, ' Guess is: ', letter_locs[d[1]])

print('Char: ', i+1, ' Guess is: ', letter_locs[d[0]])

img = io.imread('H1-16images/test1.bmp')
io.imshow(img)
ax = plt.gca()
count = 0
for props in test_regions_1:
    minr, minc, maxr, maxc = props.bbox
    height = maxr - minr
    width = maxc - minc
    if width > 10 and height > 10:
        count += 1
        ax.add_patch(Rectangle((minc, minr), maxc - minc, maxr - minr, fill = False, edgecolor = 'red', linewidth = 1))
ax.set_title('Bounding Boxes')
io.show()
print(count)
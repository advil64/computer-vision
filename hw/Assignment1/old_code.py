
# dimensionality reduction
for i, k in enumerate(normalized.keys()):
    letter_means[k] = np.mean(normalized[k], axis=0)
combined_means = np.vstack([letter_means[k] for k in letter_means])


# print('Letter: ', i+1, ' Guess is: ', letter_locs[d[1]])

print('Char: ', i+1, ' Guess is: ', letter_locs[d[0]])
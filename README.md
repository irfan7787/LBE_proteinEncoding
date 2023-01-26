# Location Based Encoding for Protein Feature Extraction

This repository contains a Python implementation of the location based encoding (LBE) method for protein feature extraction. The LBE method generates a fixed-sized feature vector for a given amino acid sequence, regardless of the length of the sequence.

Usage
To use the LBE method, simply import the LBE function from the LBE.py file and pass in a protein sequence and the desired length of the feature vector as arguments. The returned value will be a 1D numpy array containing the generated feature vector.


```python
from LBE import LBE
```python
\# Example usage
sequence = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
feature_vector = LBE(sequence, 5)

print(feature_vector)
```
# Methodology

The LBE method is based on the observation that the local composition of amino acids in a protein sequence carries important information about its function and structure. The method works by dividing the input sequence into a number of segments, and for each segment, calculating the proportion of each amino acid in the segment. The proportion values are then concatenated to form the final feature vector.

The distFeature function is used to calculate the proportion of each amino acid in a segment. It takes in a sequence as input and iterates over it, counting the occurrences of each amino acid. It then normalizes these counts by the length of the input sequence to obtain the proportions.

# References
If you use this code for your research, please cite the following paper:

[Kösesoy, İ., Gök, M., & Öz, C. (2019). A new sequence based encoding for prediction of host–pathogen protein interactions. Computational Biology and Chemistry, 78, 170-177.]

# Contact
If you have any questions or suggestions, please feel free to open an issue or contact me directly.

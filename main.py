# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 23:27:36 2023

@author: irfan kösesoy
"""

from LBE import LBE

# Example usage
sequence = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
feature_vector = LBE(sequence, 5)

print(feature_vector)
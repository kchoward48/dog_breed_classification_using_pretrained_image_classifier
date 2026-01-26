#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Kevin Howard
# DATE CREATED: 12/13/2025                                  
# REVISED DATE: 12/14/2025
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Initialize the 'results_dic':
    results_dic = dict()
    # Get filenames stored in the 'dir':
    filename_list = listdir(image_dir)
    
    # Build a list of pet names:
    pet_names = []
    for idx in range(0, len(filename_list), 1):
      # Initialize variable to built pet name string:
      pet_name = ''
      pet_image = filename_list[idx].lower()
      for word in pet_image.split('_'):
        if word.isalpha():
          pet_name += word + ' '
      pet_name = pet_name.strip()
      pet_names.append(pet_name)

    # Build out the 'results_dic':
    for idx in range(0, len(filename_list), 1):
      # Check to see if the key already exists, in case of duplicate files:
      if filename_list[idx] not in results_dic:
        results_dic[filename_list[idx]] = [pet_names[idx]]
      else:
        print('Warning: Key', filename_list[idx],
        'already exists in the results_dic with the following value =',
        results_dic[filename_list[idx]])

    # Display the first 10 filenames and their associated key in 
    # 'results_dic':
    for key in results_dic:
      print('Filename = ', key, '   Pet Label = ', results_dic[key][0])

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
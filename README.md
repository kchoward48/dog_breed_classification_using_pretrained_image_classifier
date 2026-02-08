# <kbd>module</kbd> `adjust_results4_isadog`





---

## <kbd>function</kbd> `adjust_results4_isadog`

```python
adjust_results4_isadog(results_dic, dogfile)
```

Adjusts the results dictionary to determine if classifier correctly  classified images 'as a dog' or 'not a dog' especially when not a match.  Demonstrates if model architecture correctly classifies dog images even if it gets dog breed wrong (not a match). 

**Parameters:**
  results_dic - Dictionary with 'key' as image filename and 'value' as a   List. Where the list will contain the following items:   index 0 = pet image label (string)  index 1 = classifier label (string)  index 2 = 1/0 (int)  where 1 = match between pet image  and classifer labels and 0 = no match between labels 
            ------ where index 3 & index 4 are added by this function -----  NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog. dogfile - A text file that contains names of all dogs from the classifier  function and dog names from the pet image files. This file has   one dog name per line dog names are all in lowercase with   spaces separating the distinct words of the dog name. Dog names  from the classifier function can be a string of dog names separated  by commas when a particular breed of dog has multiple dog names   associated with that breed (ex. maltese dog, maltese terrier,   maltese) (string - indicates text file's filename) 

**Returns:**
  None - results_dic is mutable data type so no return needed. 




# <kbd>module</kbd> `adjust_results4_isadog_hints`





---

## <kbd>function</kbd> `adjust_results4_isadog`

```python
adjust_results4_isadog(results_dic, dogfile)
```

Adjusts the results dictionary to determine if classifier correctly  classified images 'as a dog' or 'not a dog' especially when not a match.  Demonstrates if model architecture correctly classifies dog images even if it gets dog breed wrong (not a match). 

**Parameters:**
  results_dic - Dictionary with 'key' as image filename and 'value' as a   List. Where the list will contain the following items:   index 0 = pet image label (string)  index 1 = classifier label (string)  index 2 = 1/0 (int)  where 1 = match between pet image  and classifer labels and 0 = no match between labels 
            ------ where index 3 & index 4 are added by this function -----  NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog. dogfile - A text file that contains names of all dogs from the classifier  function and dog names from the pet image files. This file has   one dog name per line dog names are all in lowercase with   spaces separating the distinct words of the dog name. Dog names  from the classifier function can be a string of dog names separated  by commas when a particular breed of dog has multiple dog names   associated with that breed (ex. maltese dog, maltese terrier,   maltese) (string - indicates text file's filename) 

**Returns:**
  None - results_dic is mutable data type so no return needed. 




# <kbd>module</kbd> `calculates_results_stats`





---

## <kbd>function</kbd> `calculates_results_stats`

```python
calculates_results_stats(results_dic)
```

Calculates statistics of the results of the program run using classifier's model  architecture to classifying pet images. Then puts the results statistics in a  dictionary (results_stats_dic) so that it's returned for printing as to help the user to determine the 'best' model for classifying images. Note that  the statistics calculated as the results are either percentages or counts. 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string)  idx 1 = classifier label (string)  idx 2 = 1/0 (int)  where 1 = match between pet image and   classifer labels and 0 = no match between labels  idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   idx 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog. 

**Returns:**
 results_stats_dic - Dictionary that contains the results statistics (either  a percentage or a count) where the key is the statistic's   name (starting with 'pct' for percentage or 'n' for count)  and the value is the statistic's value. See comments above  and the previous topic Calculating Results in the class for details  on how to calculate the counts and statistics. 




# <kbd>module</kbd> `calculates_results_stats_hints`





---

## <kbd>function</kbd> `calculates_results_stats`

```python
calculates_results_stats(results_dic)
```

Calculates statistics of the results of the program run using classifier's model  architecture to classifying pet images. Then puts the results statistics in a  dictionary (results_stats_dic) so that it's returned for printing as to help the user to determine the 'best' model for classifying images. Note that  the statistics calculated as the results are either percentages or counts. 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string)  idx 1 = classifier label (string)  idx 2 = 1/0 (int)  where 1 = match between pet image and   classifer labels and 0 = no match between labels  idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   idx 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog. 

**Returns:**
 results_stats_dic - Dictionary that contains the results statistics (either  a percentage or a count) where the key is the statistic's   name (starting with 'pct' for percentage or 'n' for count)  and the value is the statistic's value. See comments above  and the classroom Item XX Calculating Results for details  on how to calculate the counts and statistics. 



Failed to generate docs for module check_images: ModuleNotFoundError("No module named 'print_functions_for_lab_checks'")
Failed to generate docs for module classifier: FileNotFoundError(2, 'No such file or directory')
Failed to generate docs for module classify_images: ModuleNotFoundError("No module named 'classifier'")
Failed to generate docs for module classify_images_hints: ModuleNotFoundError("No module named 'classifier'")

# <kbd>module</kbd> `get_input_args`





---

## <kbd>function</kbd> `get_input_args`

```python
get_input_args()
```

Retrieves and parses the 3 command line arguments provided by the user when they run the program from a terminal window. This function uses Python's  argparse module to created and defined these 3 command line arguments. If  the user fails to provide some or all of the 3 arguments, then the default  values are used for the missing arguments.  Command Line Arguments:  1. Image Folder as --dir with default value 'pet_images'  2. CNN Model Architecture as --arch with default value 'vgg'  3. Text File with Dog Names as --dogfile with default value 'dognames.txt' This function returns these arguments as an ArgumentParser object. 

**Parameters:**
 None - simply using argparse module to create & store command line arguments 

**Returns:**
 parse_args() -data structure that stores the command line arguments object   




# <kbd>module</kbd> `get_input_args_hints`





---

## <kbd>function</kbd> `get_input_args`

```python
get_input_args()
```

Retrieves and parses the 3 command line arguments provided by the user when they run the program from a terminal window. This function uses Python's  argparse module to created and defined these 3 command line arguments. If  the user fails to provide some or all of the 3 arguments, then the default  values are used for the missing arguments.  Command Line Arguments:  1. Image Folder as --dir with default value 'pet_images'  2. CNN Model Architecture as --arch with default value 'vgg'  3. Text File with Dog Names as --dogfile with default value 'dognames.txt' This function returns these arguments as an ArgumentParser object. 

**Parameters:**
 None - simply using argparse module to create & store command line arguments 

**Returns:**
 parse_args() -data structure that stores the command line arguments object   




# <kbd>module</kbd> `get_pet_labels`





---

## <kbd>function</kbd> `get_pet_labels`

```python
get_pet_labels(image_dir)
```

Creates a dictionary of pet labels (results_dic) based upon the filenames  of the image files. These pet image labels are used to check the accuracy  of the labels that are returned by the classifier function, since the  filenames of the images contain the true identity of the pet in the image. Be sure to format the pet labels so that they are in all lower case letters and with leading and trailing whitespace characters stripped from them. (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier') 

**Parameters:**
 image_dir - The (full) path to the folder of images that are to be  classified by the classifier function (string) 

**Returns:**
  results_dic - Dictionary with 'key' as image filename and 'value' as a   List. The list contains for following item:  index 0 = pet image label (string) 




# <kbd>module</kbd> `get_pet_labels_hints`





---

## <kbd>function</kbd> `get_pet_labels`

```python
get_pet_labels(image_dir)
```

Creates a dictionary of pet labels (results_dic) based upon the filenames  of the image files. These pet image labels are used to check the accuracy  of the labels that are returned by the classifier function, since the  filenames of the images contain the true identity of the pet in the image. Be sure to format the pet labels so that they are in all lower case letters and with leading and trailing whitespace characters stripped from them. (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier') 

**Parameters:**
 image_dir - The (full) path to the folder of images that are to be  classified by the classifier function (string) 

**Returns:**
  results_dic - Dictionary with 'key' as image filename and 'value' as a   List. The list contains for following item:  index 0 = pet image label (string) 




# <kbd>module</kbd> `print_functions_for_lab_checks`





---

## <kbd>function</kbd> `check_command_line_arguments`

```python
check_command_line_arguments(in_arg)
```

For Lab: Classifying Images - 7. Command Line Arguments Prints each of the command line arguments passed in as parameter in_arg,  assumes you defined all three command line arguments as outlined in  '7. Command Line Arguments' 

**Parameters:**
 in_arg -data structure that stores the command line arguments object 

**Returns:**
 Nothing - just prints to console   


---

## <kbd>function</kbd> `check_creating_pet_image_labels`

```python
check_creating_pet_image_labels(results_dic)
```

For Lab: Classifying Images - 9/10. Creating Pet Image Labels Prints first 10 key-value pairs and makes sure there are 40 key-value  pairs in your results_dic dictionary. Assumes you defined the results_dic dictionary as was outlined in  '9/10. Creating Pet Image Labels' 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string) 

**Returns:**
 Nothing - just prints to console   


---

## <kbd>function</kbd> `check_classifying_images`

```python
check_classifying_images(results_dic)
```

For Lab: Classifying Images - 11/12. Classifying Images Prints Pet Image Label and Classifier Label for ALL Matches followed by ALL  NOT matches. Next prints out the total number of images followed by how  many were matches and how many were not-matches to check all 40 images are processed. Assumes you defined the results_dic dictionary as was  outlined in '11/12. Classifying Images' 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string)  idx 1 = classifier label (string)  idx 2 = 1/0 (int)   where 1 = match between pet image and   classifer labels and 0 = no match between labels 

**Returns:**
 Nothing - just prints to console   


---

## <kbd>function</kbd> `check_classifying_labels_as_dogs`

```python
check_classifying_labels_as_dogs(results_dic)
```

For Lab: Classifying Images - 13. Classifying Labels as Dogs Prints Pet Image Label, Classifier Label, whether Pet Label is-a-dog(1=Yes, 0=No), and whether Classifier Label is-a-dog(1=Yes, 0=No) for ALL Matches  followed by ALL NOT matches. Next prints out the total number of images  followed by how many were matches and how many were not-matches to check  all 40 images are processed. Assumes you defined the results_dic dictionary as was outlined in '13. Classifying Labels as Dogs' 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string)  idx 1 = classifier label (string)  idx 2 = 1/0 (int)   where 1 = match between pet image and   classifer labels and 0 = no match between labels  idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   idx 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog. 

**Returns:**
 Nothing - just prints to console   


---

## <kbd>function</kbd> `check_calculating_results`

```python
check_calculating_results(results_dic, results_stats_dic)
```

For Lab: Classifying Images - 14. Calculating Results Prints First statistics from the results stats dictionary (that was created by the calculates_results_stats() function), then prints the same statistics that were calculated in this function using the results dictionary. Assumes you defined the results_stats dictionary and the statistics  as was outlined in '14. Calculating Results ' 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string)  idx 1 = classifier label (string)  idx 2 = 1/0 (int)   where 1 = match between pet image and   classifer labels and 0 = no match between labels  idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   idx 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog. results_stats_dic - Dictionary that contains the results statistics (either  a percentage or a count) where the key is the statistic's   name (starting with 'pct' for percentage or 'n' for count)  and the value is the statistic's value  

**Returns:**
 Nothing - just prints to console   




# <kbd>module</kbd> `print_results`





---

## <kbd>function</kbd> `print_results`

```python
print_results(
    results_dic,
    results_stats_dic,
    model,
    print_incorrect_dogs=False,
    print_incorrect_breed=False
)
```

Prints summary results on the classification and then prints incorrectly  classified dogs and incorrectly classified dog breeds if user indicates  they want those printouts (use non-default values) 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string)  idx 1 = classifier label (string)  idx 2 = 1/0 (int)  where 1 = match between pet image and   classifer labels and 0 = no match between labels  idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   idx 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog.  results_stats_dic - Dictionary that contains the results statistics (either  a  percentage or a count) where the key is the statistic's   name (starting with 'pct' for percentage or 'n' for count)  and the value is the statistic's value   model - Indicates which CNN model architecture will be used by the   classifier function to classify the pet images, 
 - <b>`values must be either`</b>:  resnet alexnet vgg (string) print_incorrect_dogs - True prints incorrectly classified dog images and   False doesn't print anything(default) (bool)   print_incorrect_breed - True prints incorrectly classified dog breeds and   False doesn't print anything(default) (bool)  

**Returns:**
 None - simply printing results. 




# <kbd>module</kbd> `print_results_hints`





---

## <kbd>function</kbd> `print_results`

```python
print_results(
    results_dic,
    results_stats_dic,
    model,
    print_incorrect_dogs=False,
    print_incorrect_breed=False
)
```

Prints summary results on the classification and then prints incorrectly  classified dogs and incorrectly classified dog breeds if user indicates  they want those printouts (use non-default values) 

**Parameters:**
  results_dic - Dictionary with key as image filename and value as a List   (index)idx 0 = pet image label (string)  idx 1 = classifier label (string)  idx 2 = 1/0 (int)  where 1 = match between pet image and   classifer labels and 0 = no match between labels  idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and   0 = pet Image 'is-NOT-a' dog.   idx 4 = 1/0 (int)  where 1 = Classifier classifies image   'as-a' dog and 0 = Classifier classifies image    'as-NOT-a' dog.  results_stats_dic - Dictionary that contains the results statistics (either  a  percentage or a count) where the key is the statistic's   name (starting with 'pct' for percentage or 'n' for count)  and the value is the statistic's value   model - Indicates which CNN model architecture will be used by the   classifier function to classify the pet images, 
 - <b>`values must be either`</b>:  resnet alexnet vgg (string) print_incorrect_dogs - True prints incorrectly classified dog images and   False doesn't print anything(default) (bool)   print_incorrect_breed - True prints incorrectly classified dog breeds and   False doesn't print anything(default) (bool)  

**Returns:**
 None - simply printing results. 



Failed to generate docs for module test_classifier: ModuleNotFoundError("No module named 'classifier'")

# Dataset Generator
The script aims to create a dataset from a directory of images.

The resultant _transformed_ images are of a fixed size (_width_, _height_) as specified in CLI.

The images are converted into a **row-vector** which are then inserted into output csv file(**dataset_images.csv**). The CSV file contains all the image row vectors along with the class label (_integer_ starting from 0) assigned to each row vector.

Additinally another json file is created which contains mappings of the classes of images to their respective directory names.

# USAGE
## CLI Parameters
### --src : 
Path to the source image directory.

### --w :
Width of the resultant image

### -h :
Height of the resultant image

# IMPORTANT
## Input Directory Structure
```
Main directory 
   |______image_class_1_dir
   |      |__file1.jpg
   |      |__file2.jpg
   |      |    :
   |      |__  :
   |
   |______image_class_2_dir
   |      |__file1.jpg
   |      |__file2.jpg
   |      |    :
   |      |__  :
     :
     :
     :

```

## Output Files:
### 1. Mappings.json :
```
{
    "0" : "image_class_1_dir",
    "1" : "image_class_2_dir",
     ..
     ..
     ..
     "n" : "image_class_n_dir"
}
```

### 2. dataset_images.csv
For an image(h, w) belonging to ***class 0*** is represented in the csv file as :
```
row-vector(h*w) 1, class_label
row-vector(h*w) 2, class_label
row-vector(h*w) 3, class_label
        :               :
        :               :
        :               :
row-vector(h*w) n, class_label
```

_To feed into the model the row vectors are again transformed into [h, w] matrix from the specified csv file._


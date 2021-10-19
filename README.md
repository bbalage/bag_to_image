# Bag to image

This code is designed to extract the color part of the rosbag files and save it in some image format (default to .png).

### Installation guide
First, download the repo:

```
git clone https://github.com/bbalage/bag_to_image.git
```

Enter the downloaded repo's directory.
Use pip to install the dependencies in the requirements.txt file.
Either using a virtual environment or just plainly run the command:

```
pip install -r requirements.txt
```

### Usage guide

You can run the script from the terminal.

It takes two arguments:
1. **source_directory_path**: The root directory in which you need the bag files to be converted.
2. **target_directory_path**: The target directory in which the image files should be allocated.

The script converts one bag file into 1 png (using the first frame in the bag file),
keeping the directory structure.

#### Example usage

Given directory structure:
```
directory_A
|--directory_B
|  |- file1.bag
|  |- file2.bag
|--directory_C
|  |--directory_D
|  |  |- file3.bag
|  |- file4.bag
|  |- file5.bag
```

Run command:
```
python bags_to_images.py path/to/directory_A path/to/out
```

When `out` was an empty directory somewhere, then the result should be:

```
out
|--directory_B
|  |- file1.png
|  |- file2.png
|--directory_C
|  |--directory_D
|  |  |- file3.png
|  |- file4.png
|  |- file5.png
```
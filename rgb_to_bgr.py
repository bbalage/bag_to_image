import os
import sys

import cv2


def main(source_dir, target_dir):
    content = os.listdir(source_dir)
    png_filenames = [file for file in content if file[-4:] == '.png']
    for png_filename in png_filenames:
        source_path = os.path.join(source_dir, png_filename)
        image = cv2.imread(source_path)
        result_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        target_path = os.path.join(target_dir, png_filename)
        cv2.imwrite(target_path, result_image)


if __name__ == '__main__':
    args = sys.argv
    assert len(args) >= 3
    source_dir, target_dir = args[1], args[2]
    main(source_dir, target_dir)


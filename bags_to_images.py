import os

import cv2
import numpy as np
import pyrealsense2 as rs
import sys


def extract_png_from_single_bag(path, width=1280, height=720):
    pipeline = rs.pipeline()
    config = rs.config()
    rs.config.enable_device_from_file(config, path)
    config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, 30)
    pipeline.start(config)
    frames = pipeline.wait_for_frames()
    frame = frames.get_color_frame()
    image = np.asanyarray(frame.get_data())
    pipeline.stop()
    return image


def extract_and_save_pngs_from_bags(bag_filename, target_dir, suffix='png'):
    for bag_filename in bag_filename:
        try:
            image = extract_png_from_single_bag(bag_filename)
            image_filename = bag_filename[:-3] + suffix
            target_path = os.path.join(target_dir, os.path.split(image_filename)[-1])
            cv2.imwrite(target_path, image)
            # print("Successfully converted: {0}".format(bag_filename))
        except RuntimeError:
            print("Could not retrive frame from: {0}".format(bag_filename))
            


def process_directory(source_dir, target_dir):
    content = os.listdir(source_dir)
    bags = [os.path.join(source_dir, file) for file in content if file[-4:] == '.bag']
    extract_and_save_pngs_from_bags(bags, target_dir)
    subdirectories = [file for file in content if os.path.isdir(os.path.join(source_dir, file))]
    return subdirectories


def main(source_dir, target_dir):
    directories = [source_dir]
    target_directories = [target_dir]
    while len(directories) > 0:
        inspected_directory = directories.pop()
        target_directory = target_directories.pop()
        if not os.path.exists(target_directory):
            os.mkdir(target_directory)
        new_directories = process_directory(inspected_directory, target_directory)
        directories += [os.path.join(inspected_directory, directory) for directory in new_directories]
        target_directories += [os.path.join(target_directory, directory) for directory in new_directories]


if __name__ == '__main__':
    args = sys.argv
    assert len(args) >= 3
    source_dir, target_dir = args[1], args[2]
    main(source_dir, target_dir)

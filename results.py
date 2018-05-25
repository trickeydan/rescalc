#! /usr/bin/env python3

import argparse
from reslib import Course

parser = argparse.ArgumentParser(description="Result Calculator")

parser.add_argument("course_folder", help="Directory for course folder")

args = parser.parse_args()

course = Course(args.course_folder)
#! /usr/bin/env python3

import argparse
from reslib import Course


def print_course_info(course):
    print("Course Name: ", course.name)


FUNCTION_MAP = {'info': print_course_info}

parser = argparse.ArgumentParser(description="Result Calculator")
parser.add_argument("course_folder", help="Directory for course folder")
parser.add_argument("command", help="Command to run", choices=FUNCTION_MAP.keys())

args = parser.parse_args()

course = Course(args.course_folder)

func = FUNCTION_MAP[args.command]
func(course)

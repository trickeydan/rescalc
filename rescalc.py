#! /usr/bin/env python3

import argparse
from reslib import Course

def print_course_info(course):
    print("Name:", course.name)
    print("Score:", course.score, "%")
    print("Classification:", course.classification)
    print("The course has", len(course.parts), "parts")

def print_all_info(course):
    print_course_info(course)
    for part in course.parts:
        print("\t",round(part.score, 1), "-", part.name, "Class:", part.classification)
        for sem in part.semesters:
            print("\t\t", round(sem.score, 1), "-", sem.name, "Class:", sem.classification)
            for mod in sem.modules:
                print("\t\t\t", round(mod.score, 1), "-", mod.name, "Class:", mod.classification)
                for assess in mod.assessments:
                    print("\t\t\t\t", round(assess.score, 1), "-", assess.name, "Class:", assess.classification)

FUNCTION_MAP = {
    'all': print_all_info,
    'course': print_course_info
}

parser = argparse.ArgumentParser(description="Result Calculator")
parser.add_argument("course_folder", help="Directory for course folder")
parser.add_argument("command", help="Command to run", choices=FUNCTION_MAP.keys())

args = parser.parse_args()

course = Course(args.course_folder)

func = FUNCTION_MAP[args.command]
func(course)

#! /usr/bin/env python3

import argparse
from reslib import Course


def print_course_info(course):
    print("Name:", course.name)
    print("Score:", course.score, "%")
    print("Classification:", course.classification)
    print("The course has", len(course.parts), "parts:")
    for part in course.parts:
        print("\t", part.name, "(", part.score, ")")
        for sem in part.semesters:
            print("\t\t", sem.name, "(", sem.score, ")")
            for mod in sem.modules:
                print("\t\t\t", mod.name, "(", mod.score, ")")
                for assess in mod.assessments:
                    print("\t\t\t\t", assess.name, "(", assess.score, ")")


FUNCTION_MAP = {
    'info': print_course_info,
}

parser = argparse.ArgumentParser(description="Result Calculator")
parser.add_argument("course_folder", help="Directory for course folder")
parser.add_argument("command", help="Command to run", choices=FUNCTION_MAP.keys())

args = parser.parse_args()

course = Course(args.course_folder)

func = FUNCTION_MAP[args.command]
func(course)

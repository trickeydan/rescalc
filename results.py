#! /usr/bin/env python3

import yaml, argparse, os



parser = argparse.ArgumentParser(description="Result Calculator")

parser.add_argument("course", help="Name of course folder")

args = parser.parse_args()

with open(os.path.join(args.course,"course.yml"), "r") as course_file:
    try:
        course = yaml.load(course_file)

        for part in course["parts"]:
            print(part["name"])
            for semester in part["semesters"]:
                print(" ", semester["name"])
                if not semester["modules"] is None:
                    for module_name in semester["modules"]:
                        # print("     ", module)
                        with open(os.path.join(args.course,"modules",module_name + ".yml"), "r") as module_file:
                            try:
                                module = yaml.load(module_file)
                                print("     ", module["name"], " - ", module_name)
                                for assessment in module["assessments"]:
                                    print("         ",assessment["name"])
                            except yaml.YAMLError as e:
                                print("Could not parse yaml")
                                print(e)
    except yaml.YAMLError as e:
        print("Could not parse yaml")
        print(e)

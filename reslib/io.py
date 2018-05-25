import sys
import yaml


def loadfile(filename):
    try:
        with open(filename, "r") as course_file:
            data = yaml.load(course_file)
            return data
    except FileNotFoundError:
        sys.exit("course.yml could not be found")
    except yaml.YAMLError:
        sys.exit("course.yml contained invalid YAML")
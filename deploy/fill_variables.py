#! /usr/bin/env python3

import os
import re
import sys


def fill_variable(match_obj):
    if "CIRCLE_SHA1" in match_obj.group(1):
        return os.environ["CIRCLE_SHA1"][:7]
    return os.environ[match_obj.group(1)]


def main(argv):
    new_file = ""
    with open(argv[1]) as template_script:
        for line in template_script.readlines():
            new_file += re.sub(r"\$\{([\:\w\d]+)\}", fill_variable, line)

    with open(argv[1] + "_filled", "w+") as filled:
        filled.write(new_file)


if __name__ == "__main__":
    main(sys.argv)

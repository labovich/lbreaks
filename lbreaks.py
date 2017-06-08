#!/usr/bin/env python3

import sys
import getopt

conf = {}


def replace_breaks(string, mode):
    if mode:
        result = string.replace("\r\n", "\n")
    else:
        result = string.replace("\n", "\r\n")
    return result


def open_files(in_f, out_f):
    with open(in_f, 'r') as f_in:
        with open(out_f, 'w') as f_out:
            for line in f_in:
                f_out.write(replace_breaks(line, conf["mode"]))


def get_options(opt_list):
    conf["mode"] = True

    for opt in opt_list:
        if opt[0] == "-i":
            conf["in_file"] = opt[1]
        if opt[0] == "-o":
            conf["out_file"] = opt[1]
        if opt[0] == "-d":
            conf["mode"] = False
        if opt[0] in ["-h", "--help"]:
            show_help()
            sys.exit(0)
        if opt[0] in ["-V", "--version"]:
            show_version()
            sys.exit(0)


def show_help():
    show_version()
    print("Small command line tool for convert line breaks from UNIX format to DOS format or")
    print("from DOS format to UNIX format.")
    print("GitHub https://github.com/labovich/lbreaks")
    print()
    print("Usage: {} -i <input file> -o <output file>".format(sys.argv[0]))
    print()
    print("Options:")
    print("    -i <filename>    input file")
    print("    -o <filename>    output file")
    print("    -d               convert from UNIX format to DOS format")
    print("                     (default convert from DOS format to UNIX format)")
    print("    -h, --help       display this help message")
    print("    -V, --version    print the version")
    print()


def show_version():
    print("lbreaks version 0.1")


def main(args):
    cmd_opts = 'i:o:ud'
    cmd_lopts = ['help', 'version']

    if len(args) < 2:
        show_help()
        sys.exit(0)

    try:
        opt_list, args = getopt.getopt(args[1:], cmd_opts, cmd_lopts)
    except getopt.GetoptError:
        show_help()
        sys.exit(1)

    get_options(opt_list)

    if "in_file" not in conf or "out_file" not in conf:
        show_help()
        sys.exit(0)

    try:
        open_files(conf["in_file"], conf["out_file"])
    except (FileNotFoundError, FileExistsError, PermissionError, IsADirectoryError) as err:
        print(err)
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)

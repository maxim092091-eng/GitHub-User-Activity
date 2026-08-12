import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("name")
    parser.add_argument("params", nargs="*")

    return parser.parse_args()
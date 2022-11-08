import os
import argparse

def main(args):
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--allow-rotation', default = False, help = 'TODO')
    parser.add_argument('--model_name', default = 'model', help = 'TODO')
    parser.add_argument('--symmetry-breaking-constraints', default = False, help = 'TODO')
    args = parser.parse_args()

    main(args)


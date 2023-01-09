import argparse


def pars_input_args():
    parser = argparse.ArgumentParser(
        description='Analyze data.',
        prog='data-analysis'
    )
    parser.add_argument(
        '--file-path',
        dest='file_path',
        default=None,
        type=str,
        help='file path of input data',
    )

    return parser.parse_args()

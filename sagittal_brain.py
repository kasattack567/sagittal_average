from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import numpy as np

def run_averages(file_input='brain_sample.csv', file_output='brain_average.csv'):
    """
    Calculates the average through the coronal planes.
    Each column corresponds to a coronal plane;
    each row corresponds to a sagittal/horizontal intersection.
    """
    # Read input CSV
    with open(file_input, 'r') as myfile:
        planes = [list(map(int, line.strip().split(','))) for line in myfile]

    planes = np.array(planes)
    averages = np.mean(planes, axis=0)

    # Save output correctly (single CSV row)
    np.savetxt(file_output, [averages], fmt='%.2f', delimiter=',')


if __name__ == "__main__":
    parser = ArgumentParser(description="Calculates the average for each sagittal-horizontal plane.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default="brain_sample.csv",
                        help="Input CSV file with the results from scikit-brain binning algorithm.")
    parser.add_argument('--file_output', '-o', default="brain_average.csv",
                        help="Name of the output CSV file.")
    arguments = parser.parse_args()

    run_averages(arguments.file_input, arguments.file_output)

import sys
import os


def update_lammps_input(input_file, data_file_path):
    output_file = os.path.splitext(data_file_path)[0] + ".in"
    base_dir = os.path.dirname(data_file_path)  # Get the directory of the data file
    airebo_file = os.path.join(base_dir, "CH.airebo")  # Dynamically locate CH.airebo in the same folder

    print(f"Base directory: {base_dir}")
    print(f"Data file path: {data_file_path}")
    print(f"AIREBO file path: {airebo_file}")

    with open(input_file, 'r') as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        # Update log file path
        if line.startswith("log "):
            line = f"log {data_file_path.replace('.data', '_forDeforminZdirection.log')}\n"

        # Update read_data path
        if line.startswith("read_data"):
            line = f"read_data {data_file_path}\n"

        # Update dump file path
        if line.startswith("dump "):
            dump_path = data_file_path.replace('.data', '_DumpforDeforminZdirection.lammpstrj')
            line = f"dump 1 all atom 2000 {dump_path}\n"

        # Update pair_coeff path dynamically
        if line.startswith("pair_coeff"):
            line = f"pair_coeff * * {airebo_file} C\n"

        updated_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(updated_lines)

    print(f"Updated LAMMPS .in file saved as {output_file}")


if __name__ == "__main__":
    input_file = sys.argv[1]
    data_file_path = sys.argv[2]
    update_lammps_input(input_file, data_file_path)

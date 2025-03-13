import sys
import os


def update_lammps_input(input_file, data_file_path):
    output_file = os.path.splitext(data_file_path)[0] + ".in"
    base_dir = os.path.dirname(os.path.abspath(data_file_path))  # Get absolute directory of the data file
    airebo_file = os.path.join(base_dir, "CH.airebo")  # Dynamically locate CH.airebo in the same folder
    log_file = os.path.splitext(data_file_path)[0] + "_forDeforminZdirection.log"
    dump_file = os.path.splitext(data_file_path)[0] + "_DumpforDeforminZdirection.lammpstrj"
    dump_file_abs = os.path.abspath(dump_file)

    # Print all paths for verification
    print(f"Base directory: {base_dir}")
    print(f"Data file path: {os.path.abspath(data_file_path)}")
    print(f"AIREBO file path: {airebo_file}")
    print(f"Log file path: {log_file}")
    print(f"Dump file path: {dump_file_abs}")

    with open(input_file, 'r') as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        # Update log file path
        if line.startswith("log "):
            line = f"log {log_file}\n"

        # Update read_data path with absolute path
        if line.startswith("read_data"):
            line = f"read_data \"{os.path.abspath(data_file_path)}\"\n"

        # Update dump file path with absolute path
        if line.startswith("dump "):
            line = f"dump 1 all atom 2000 \"{dump_file_abs}\"\n"

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

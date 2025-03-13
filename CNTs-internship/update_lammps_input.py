import sys


def update_lammps_input(input_file, output_file, data_file_path):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        # Update log file path
        if line.startswith("log "):
            line = f"log {data_file_path.replace('.data', '.lammps')}\n"

        # Update read_data path
        if line.startswith("read_data"):
            line = f"read_data {data_file_path}\n"

        # Update dump file path
        if line.startswith("dump "):
            dump_path = data_file_path.replace('.data', '_forDeforminZdirection.lammpstrj')
            line = f"dump 1 all atom 2000 {dump_path}\n"

        updated_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(updated_lines)

    print(f"Updated LAMMPS .in file saved as {output_file}")


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_file_path = sys.argv[3]
    update_lammps_input(input_file, output_file, data_file_path)

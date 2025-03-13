import sys


def convert_lammpstrj_to_data(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    timestep_idx = lines.index("ITEM: TIMESTEP\n")
    num_atoms_idx = lines.index("ITEM: NUMBER OF ATOMS\n")
    box_bounds_idx = lines.index("ITEM: BOX BOUNDS pp pp pp\n")
    atoms_idx = lines.index("ITEM: ATOMS id type xu yu zu\n")

    # Extract number of atoms
    num_atoms = int(lines[num_atoms_idx + 1].strip())

    # Extract box bounds
    x_bounds = list(map(float, lines[box_bounds_idx + 1].split()))
    y_bounds = list(map(float, lines[box_bounds_idx + 2].split()))
    z_bounds = list(map(float, lines[box_bounds_idx + 3].split()))

    # Extract atom data
    atom_data = []
    for i in range(atoms_idx + 1, atoms_idx + 1 + num_atoms):
        atom_data.append(lines[i].strip())

    # Convert to .data format
    with open(output_file, 'w') as f:
        f.write("Uniaxial Tensile Test of Graphene CNT\n\n")
        f.write(f"{num_atoms} atoms\n\n")
        f.write("1 atom types\n\n")
        
        f.write("#simulation box\n")
        f.write(f"{x_bounds[0]} {x_bounds[1]} xlo xhi\n")
        f.write(f"{y_bounds[0]} {y_bounds[1]} ylo yhi\n")
        f.write(f"{z_bounds[0]} {z_bounds[1]} zlo zhi\n\n")

        f.write("Masses\n\n")
        f.write("1 12.010000\n\n")

        f.write("Atoms\n\n")
        for atom in atom_data:
            f.write(atom + "\n")

    print(f"Converted .lammpstrj file to .data format and saved as {output_file}")


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_lammpstrj_to_data(input_file, output_file)

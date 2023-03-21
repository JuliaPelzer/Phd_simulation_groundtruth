import numpy as np
import os
import sys
import make_general_settings as mgs

if __name__ == "__main__":

    param_dataset_size = int(sys.argv[1])
    dataset_folder = sys.argv[2]
    number_of_hps = 1
    if bool(sys.argv[3]):
        number_of_hps = 2

    # get boundaries of domain
    settings = mgs.load_settings(dataset_folder, file_name="settings")
    grid_size = settings["grid"]["size"]

    for i in range(number_of_hps):
        # choose random position inside domain
        locs_x = np.random.randint(0, grid_size[0], param_dataset_size)
        locs_y = np.random.randint(0, grid_size[1], param_dataset_size)

        # save to file
        with open(os.path.join(dataset_folder, f"locs_hp_x_{i+1}.txt"), "w") as f:
            np.savetxt(f, locs_x)
        with open(os.path.join(dataset_folder, f"locs_hp_y_{i+1}.txt"), "w") as f:
            np.savetxt(f, locs_y)   
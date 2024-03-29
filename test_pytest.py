# run pytest from unittests folder
import os
import subprocess

import numpy as np

import scripts.make_general_settings as script_settings
from scripts.create_grid_unstructured import write_loc_well_file

# def test_run_bash_pressure_1D_permeability():
# 	assert os.getcwd() == "/home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth", "wrong working directory"

# 	subprocess.call("cp unittests/input_pflotran_files/pflotran_vary_perm.in pflotran.in", shell=True)
# 	for i in [1,2]:
# 		number_vary_pressure = i
# 		for j in [1,2]:
# 			number_vary_perm = j
# 			subprocess.call(f"bash make_dataset.sh {number_vary_pressure} 1D {number_vary_perm} vary 3D test_bash_perm", shell=True)
# 			assert _fcount("test_bash_perm") == number_vary_pressure*number_vary_perm + 1, "perm test created the wrong number of datapoints"
# 			assert os.path.isfile("test_bash_perm/inputs/settings.yaml"), "settings.yaml not found"
# 			os.system("rm -r test_bash_perm")
# 	for temp_file in ["pflotran.in", "mesh.uge", "north.ex", "south.ex", "west.ex", "east.ex", "heatpump_inject1.vs"]:
# 		os.system(f"rm {temp_file}")
# 	os.system("rm -r __pycache__")


def test_run_make_benchmark():
    assert (
        os.getcwd()
        == "/home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth"
    ), "wrong working directory"
    numbers_datapoints = [1, 2]
    for number_datapoints in numbers_datapoints:
        subprocess.call(
            f"bash make_benchmark.sh {number_datapoints} test_bash_perm no_vis false false",
            shell=True,
        )
        assert (
            _fcount("test_bash_perm") == number_datapoints + 1
        ), "perm test created the wrong number of datapoints"
        for file in [
            "settings.yaml",
            "permeability_values.txt",
            "pflotran_copy.in",
            "pressure_values.txt",
        ]:
            assert os.path.isfile(f"test_bash_perm/inputs/{file}"), f"{file} not found"
        os.system("rm -r test_bash_perm")
        for temp_file in [
            "pflotran.in",
            "mesh.uge",
            "north.ex",
            "south.ex",
            "west.ex",
            "east.ex",
            "heatpump_inject1.vs",
        ]:
            os.system(f"rm {temp_file}")
    os.system("rm -r __pycache__")


def test_run_make_benchmark_hp_vary():
    assert (
        os.getcwd()
        == "/home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth"
    ), "wrong working directory"
    number_datapoints = 2
    subprocess.call(
        f"bash make_benchmark.sh {number_datapoints} test_bash_perm no_vis true false",
        shell=True,
    )
    assert (
        _fcount("test_bash_perm") == number_datapoints + 1
    ), "perm test created the wrong number of datapoints"
    for file in [
        "settings.yaml",
        "locs_hp_x_1.txt",
        "locs_hp_y_1.txt",
        "permeability_values.txt",
        "pflotran_copy.in",
        "pressure_values.txt",
    ]:
        assert os.path.isfile(f"test_bash_perm/inputs/{file}"), f"{file} not found"
    os.system("rm -r test_bash_perm")
    for temp_file in [
        "pflotran.in",
        "mesh.uge",
        "north.ex",
        "south.ex",
        "west.ex",
        "east.ex",
        "heatpump_inject1.vs",
    ]:
        os.system(f"rm {temp_file}")
    os.system("rm -r __pycache__")


def test_run_make_benchmark_hp_vary_2hps():
    assert (
        os.getcwd()
        == "/home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth"
    ), "wrong working directory"
    number_datapoints = 2
    subprocess.call(
        f"bash make_benchmark.sh {number_datapoints} test_bash_perm no_vis true true",
        shell=True,
    )
    assert (
        _fcount("test_bash_perm") == number_datapoints + 1
    ), "perm test created the wrong number of datapoints"
    for file in [
        "settings.yaml",
        "locs_hp_x_1.txt",
        "locs_hp_y_1.txt",
        "locs_hp_x_2.txt",
        "locs_hp_y_2.txt",
        "permeability_values.txt",
        "pflotran_copy.in",
        "pressure_values.txt",
    ]:
        assert os.path.isfile(f"test_bash_perm/inputs/{file}"), f"{file} not found"
    os.system("rm -r test_bash_perm")
    for temp_file in [
        "pflotran.in",
        "mesh.uge",
        "north.ex",
        "south.ex",
        "west.ex",
        "east.ex",
        "heatpump_inject1.vs",
    ]:
        os.system(f"rm {temp_file}")
    os.system("rm -r __pycache__")


def test_create_grid():
    os.getcwd()
    try:
        os.mkdir("test_grid")
    except:
        pass
    subprocess.call(
        f"python3 /home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth/scripts/create_grid_unstructured.py /home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth/unittests/test_grid/",
        shell=True,
    )
    os.system("rm -r test_grid")
    os.system("rm -r __pycache__")


def test_create_grid_different_size():
    os.getcwd()
    try:
        os.mkdir("test_grid_small")
    except:
        pass
    grid_widths = [200, 200, 200]
    number_cells = [2, 3, 6]
    subprocess.call(
        f"python3 /home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth/scripts/create_grid_unstructured.py /home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth/unittests/test_grid_small/ 3D {grid_widths[0]} {grid_widths[1]} {grid_widths[2]} {number_cells[0]} {number_cells[1]} {number_cells[2]}",
        shell=True,
    )
    subprocess.call(
        "bash ../make_dataset.sh 1 1D 1 vary 3D test_grid_small", shell=True
    )
    # TODO actual ASSERT
    # TODO interaction with bash script
    os.system("rm -r test_grid_small")
    os.system("rm -r __pycache__")


def test_create_and_change_settings():
    path = "/home/pelzerja/Development/simulation_groundtruth_pflotran/Phd_simulation_groundtruth/unittests/"

    settings_changed = script_settings.main_change_grid_size(
        path,
        case="",
        name_file="settings_mini",
        grid_widths=[200, 200, 200],
        number_cells=[10, 10, 10],
        frequency=[2, 2, 2],
    )
    settings_default = script_settings.load_yaml(
        path, file_name="settings_default_mini"
    )

    assert (
        settings_default == settings_changed
    ), "settings_default and settings_changed are not equal"
    subprocess.call("rm settings_mini.yaml", shell=True)


def test_loc_well():
    settings = {"grid": {"ncells": [10, 10, 10], "size": [200, 200, 200]}}
    path_to_output = "."
    loc_hp = np.array([1, 0, 0])
    # Fixture
    true_id = 1
    # Result
    result_id = write_loc_well_file(path_to_output, settings, loc_hp)
    assert true_id == result_id, "wrong id"

    # Fixture
    true_id = 11
    loc_hp = np.array([39, 41, 0])
    # Result
    result_id = write_loc_well_file(path_to_output, settings, loc_hp)
    assert true_id == result_id, "wrong id"

    # Fixture
    true_id = 1000
    loc_hp = np.array([200, 200, 200])
    # Result
    result_id = write_loc_well_file(path_to_output, settings, loc_hp)
    assert true_id == result_id, "wrong id"


def _fcount(path):
    count = 0
    for f in os.listdir(path):
        child = os.path.join(path, f)
        if os.path.isdir(child):
            count += +1
    return count


if __name__ == "__main__":
    # test_run_bash_pressure_1D_permeability()
    test_loc_well()

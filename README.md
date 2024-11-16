# Analysis Framework

This framework processes DAOD PHYSLITE ROOT files, extracts relevant variables, applies predefined cuts, and saves the selected data back into a new ROOT file. The primary goal is to provide an easy-to-use setup for collecting and saving variables, which are commonly used in high-energy physics analysis.

  ```bash
  git clone https://gitlab.cern.ch/mdidenko/analysisframeworktsu.git AnalysisFramework
  ```

## Framework Structure

The framework is divided into several modules, each responsible for different tasks. Here’s an overview of the project structure

### Main Components

#### `config/settings.py`
This file contains all the configuration settings required for the analysis, including:

- **Input Files**: A list of ROOT files to process.
- **Output File Naming**: A function to generate output filenames based on input files.
- **Preselection Cuts**: Definitions of cuts for selecting electrons, muons, and other variables.
- **Branches**: The list of variables (branches) that will be extracted from the input ROOT files.

#### `src/NtupleWriter.py`

This file contains the core function to save collected variables to a new ROOT file:

- **`save_to_root(output_filename, all_vars)`**: This function takes the collected variables (`all_vars`), creates ROOT branches for each variable, fills the branches with data, and saves everything in a new ROOT file. It also ensures that the event number and other variables are saved in the correct format.

#### `src/VariableCollector.py`

This file contains the function to collect the necessary variables from a given ROOT file:

- **`collect_variables(tree, branches)`**: This function reads the branches defined in `settings.py`, extracts the corresponding variables from the ROOT tree, and returns them in a dictionary. The variables are converted to awkward arrays using the `awkward` library.

#### `scripts/run_analysis.py`

This is the main script to execute the analysis. It reads input files, collects variables from the ROOT trees, applies any necessary cuts, and saves the selected data to a new ROOT file.

- **Command-line Arguments**: The script allows the user to specify the input files, output directory, debug mode, and the maximum number of events to process.

- **Processing Flow**:
  1. Open the ROOT files.
  2. Collect the defined variables from the ROOT trees.
  3. Apply cuts (if any).
  4. Save the collected variables to a new ROOT file.

#### `outputs/`

This directory is where the processed ROOT files are saved after the analysis is completed.

#### `data/`

This directory can contain sample input DAOD PHYSLITE ROOT files or any necessary data files needed for the analysis.

### How to Run the Code

Follow the steps below to set up the environment and run the analysis:

1. **Set Up Conda Environment**
   - You can use the `conda` environment:
     ```bash
      cwget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh # only the first time you install
      bash Miniconda3-latest-Linux-x86_64.sh # when prompted, type 'yes', ENTER, 'yes' etc..
      source ~/.bashrc
      conda create -n py3 python=3 pip
      conda activate py3
      conda install -c conda-forge root #install root
     ```
   - This installation allows you to write the ntuple using `TTree`.

2. **Configure Your Python Environment**
   - Ensure that your `PYTHONPATH` is correctly set up. Modify the `PYTHONPATH` variable in the `setup.sh` file to match your environment and system setup.
   - To set up the environment, run the following:
     ```bash
     source setup.sh
     ```

3. **Run the Analysis**
   - Now you're ready to run the analysis. Use the following command to execute the script:
     ```bash
     python scripts/run_analysis.py --input_files data/mc/DAOD_PHYSLITE.37620644._000013.pool.root.1 --output_dir outputs/ --debug
     ```

   - **Arguments:**
     - `--input_files`: A comma-separated list of input ROOT files to process.
     - `--output_dir`: The directory where the processed ROOT files will be saved.
     - `--max_events`: *(Optional)* The maximum number of events to process. If not provided, all events will be processed.
     - `--debug`: *(Optional)* Enable debug mode to process only the first 1000 events for faster debugging.

   This will process the input ROOT file `DAOD_PHYSLITE.37620644._000013.pool.root.1`, apply any necessary cuts, and save the results to the `outputs/` directory. The `--debug` flag ensures only the first 1000 events are processed for debugging.

5. **Check Output**
   - After running the analysis, check the `outputs/` directory for the processed ROOT files. The filenames will be automatically generated based on the input ROOT file names and the configuration in `settings.py`.
   
   Example output filename: ntuple.37620644._000013_pool.root
   
The output ROOT file will contain a TTree with branches for each of the selected variables such as `eventNumber`, `el_pt`, `jet_pt`, `mu_pt`, etc.

By following these steps, you'll be able to run the analysis framework, process input ROOT files, apply the necessary cuts, and save the selected data into new ROOT files for further analysis.

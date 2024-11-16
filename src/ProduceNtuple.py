# AnalysisFramework/src/ProduceNtuple.py

import uproot3
import numpy as np
from AnalysisFramework.src import open_root_file, collect_variables, apply_electron_preselection, apply_muon_preselection, save_to_root
from AnalysisFramework import config.settings as cfg

def main():
    # Collecting variables from all input ROOT files
    all_vars = {}
    
    for file_path in cfg.input_files:
        print(f"Loading file: {file_path}")
        with uproot3.open(file_path) as file:
            tree = open_root_file(file)

            # Collecting variables from the ROOT tree
            variables = collect_variables(tree, cfg.branches)

            # Apply preselection cuts
            preselected_electrons = apply_electron_preselection(variables, cfg.preselection_cuts)
            preselected_muons = apply_muon_preselection(variables, cfg.preselection_cuts)

            # Store preselected events
            all_vars["preselected_electrons"] = preselected_electrons
            all_vars["preselected_muons"] = preselected_muons

    # Generate the output filename dynamically
    output_filename = cfg.generate_output_filename(cfg.input_files[0])  # You can loop over files if needed
    print(f"Output filename: {output_filename}")
    
    # Save the selected events into a ROOT file
    save_to_root(output_filename, all_vars)

if __name__ == "__main__":
    main()
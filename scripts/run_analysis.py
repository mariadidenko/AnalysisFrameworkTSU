#!/usr/bin/env python
# run_analysis.py

import argparse
import uproot
import awkward as ak
from src import open_root_file, collect_variables, save_to_root
from config import settings  # Assuming settings contains the necessary configurations
import os
import time

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Run the analysis and save variables to ROOT file.")
    parser.add_argument('--input_files', type=str, required=True, help="Path to the input ROOT files (comma-separated list)")
    parser.add_argument('--output_dir', type=str, required=True, help="Directory to save the output")
    parser.add_argument('--debug', action='store_true', help="Enable debug output (process max 1000 events)")
    parser.add_argument('--max_events', type=int, default=None, help="Maximum number of events to process")
    args = parser.parse_args()

    # Convert input files to a list (comma-separated in case of multiple files)
    input_files = args.input_files.split(',')

    # Set a limit for events in debug mode
    max_events = args.max_events if args.max_events else (1000 if args.debug else None)

    # Loop over each input file
    for input_file in input_files:
        print(f"Loading file: {input_file}")
        
        # Open the ROOT file and collect the variables
        tree = open_root_file(input_file)

        # Collect variables from the ROOT file using branches defined in settings.py
        branches = settings.branches
        print(f"Collecting variables from branches: {branches}")
        variables = collect_variables(tree, branches)

        # Apply the max_events limit if in debug mode or if a max_events argument is provided
        if max_events:
            print(f"Debug mode: Processing only the first {max_events} events.")
            for key in variables.keys():
                variables[key] = variables[key][:max_events]

        # Prepare the data to be saved
        all_vars = {}

        # Add variables dynamically (make sure they exist in the data)
        if "eventNumber" in variables:
            all_vars["eventNumber"] = variables["eventNumber"]
        if "el_pt" in variables:
            all_vars["el_pt"] = variables["el_pt"]
        if "el_eta" in variables:
            all_vars["el_eta"] = variables["el_eta"]
        if "el_phi" in variables:
            all_vars["el_phi"] = variables["el_phi"] 
        if "el_charge" in variables:
            all_vars["el_charge"] = variables["el_charge"]    
        if "mu_pt" in variables:
            all_vars["mu_pt"] = variables["mu_pt"]
        if "mu_eta" in variables:
            all_vars["mu_eta"] = variables["mu_eta"]
        if "mu_phi" in variables:
            all_vars["mu_phi"] = variables["mu_phi"]
        if "mu_charge" in variables:
            all_vars["mu_charge"] = variables["mu_charge"]     
        if "jet_pt" in variables:
            all_vars["jet_pt"] = variables["jet_pt"]
        if "jet_eta" in variables:
            all_vars["jet_eta"] = variables["jet_eta"]
        if "jet_phi" in variables:
            all_vars["jet_phi"] = variables["jet_phi"]
        if "jet_mass" in variables:
            all_vars["jet_mass"] = variables["jet_mass"]    
        if "btag_prob" in variables:
            all_vars["btag_prob"] = variables["btag_prob"]

        # Construct the output filename using the settings for that file
        output_filename = os.path.join(args.output_dir, settings.generate_output_filename(input_file))
        print(f"Saving output to: {output_filename}")
        
        # Save the results to ROOT
        save_to_root(output_filename, all_vars)

        # Debug output
        if args.debug:
            print(f"Processed {len(variables.get('eventNumber', []))} events")

if __name__ == "__main__":
    main()





# AnalysisFramework/src/NtupleWriter.py

import ROOT
import awkward as ak
import numpy as np

def save_to_root(output_filename, all_vars):
    """Save the collected variables to a ROOT file using ROOT.TTree."""
    
    # Open a ROOT file to save data
    root_file = ROOT.TFile(output_filename, "RECREATE")
    
    # Create an empty ROOT TTree
    tree = ROOT.TTree("tree", "AnalysisTree")
    
    # Create ROOT branches
    event_number_branch = ROOT.vector('int')()  # Vector for event number branch
    tree.Branch("eventNumber", event_number_branch)

    # Handle event numbers (only once per event)
    if "eventNumber" in all_vars:
        event_numbers = ak.to_list(all_vars["eventNumber"])  # Convert awkward Array to list
        for event_number in event_numbers:
            event_number_branch.clear()  # Clear the branch vector before appending
            event_number_branch.push_back(event_number)  # Append the event number
    
    # Prepare branches for other variables (el_pt, jet_pt, mu_pt, etc.)
    variable_branches = {}

    # Handle each variable type (el_pt, jet_pt, mu_pt, mu_eta, etc.)
    for var_name in all_vars:
        if var_name == "eventNumber":  # Skip eventNumber as it's already handled
            continue
        
        # Convert awkward array to list of lists
        variable_data = ak.to_list(all_vars[var_name])  
        
        # Create a vector for this variable
        branch_data = ROOT.vector('float')()
        tree.Branch(var_name, branch_data)
        
        # Store the variable branches in a dictionary for later use
        variable_branches[var_name] = (branch_data, variable_data)
    
    # Now process each event and fill the tree
    num_events = len(event_numbers)
    for i in range(num_events):
        # Fill data for the current event
        for var_name, (branch_data, variable_data) in variable_branches.items():
            branch_data.clear()  # Clear the vector for the current variable
            data = variable_data[i]  # Get the data for this event (e.g., a list of values)
            for value in data:
                branch_data.push_back(value)  # Append value to the branch

        # Fill the event number (it should be the same for each variable in this event)
        tree.Fill()  # Only fill once per event

    # Write the tree and close the ROOT file
    root_file.Write()
    root_file.Close()
    print(f"Data saved to {output_filename}")





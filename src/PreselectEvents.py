# AnalysisFramework/src/PreselectEvents.py

import awkward as ak

def apply_electron_preselection(variables, preselection_cuts):
    # Create an empty list to store preselected electrons
    preselected_electrons = []

    # Loop through each electron and apply the preselection cuts
    for i in range(len(variables["el_pt"])):
        # Apply pt and eta cuts for electrons
        pt_pass = variables["el_pt"][i] > preselection_cuts["electron_pt_cut"]
        eta_pass = abs(variables["el_eta"][i]) < preselection_cuts["electron_eta_cut"]

        # Use ak.any() to check if any of the electron's variables pass the cuts
        if ak.any(pt_pass) and ak.any(eta_pass):
            preselected_electrons.append(variables["el_pt"][i])  # Keep the electron if it passes the preselection
        else:
            preselected_electrons.append(-1)  # Mark as -1 if the electron fails

    return preselected_electrons

def apply_muon_preselection(variables, preselection_cuts):
    # Create an empty list to store preselected muons
    preselected_muons = []

    # Loop through each muon and apply the preselection cuts
    for i in range(len(variables["mu_pt"])):
        # Apply pt and eta cuts for muons
        pt_pass = variables["mu_pt"][i] > preselection_cuts["muon_pt_cut"]
        eta_pass = abs(variables["mu_eta"][i]) < preselection_cuts["muon_eta_cut"]

        # Use ak.any() to check if any of the muon's variables pass the cuts
        if ak.any(pt_pass) and ak.any(eta_pass):
            preselected_muons.append(variables["mu_pt"][i])  # Keep the muon if it passes the preselection
        else:
            preselected_muons.append(-1)  # Mark as -1 if the muon fails

    return preselected_muons

# config/settings.py

import os

# Input ROOT file paths (list of files)
input_files = [
    "/lhome/ific/m/mdidenko/work/ATLASOpenData/ResearchPurpose/NtupleMaker/AnalysisFramework/data/mc/DAOD_PHYSLITE.37620644._000013.pool.root.1",
    "/lhome/ific/m/mdidenko/work/ATLASOpenData/ResearchPurpose/NtupleMaker/AnalysisFramework/data/mc/DAOD_PHYSLITE.37620644._000014.pool.root.1"
]

# Output file path generation function
def generate_output_filename(input_file):
    filename = os.path.basename(input_file)
    parts = filename.split(".")
    output_filename = f"ntuple.{parts[1]}.{parts[2]}_{parts[3]}.root"
    return output_filename

# Preselection cuts for electrons and muons
preselection_cuts = {
    "electron_pt_cut": 35000,  # pt cut for electrons (in MeV)
    "electron_eta_cut": 2.47,  # eta cut for electrons
    "muon_pt_cut": 35000,      # pt cut for muons
    "muon_eta_cut": 2.5        # eta cut for muons
}

# Branch names for extraction
branches = {
    "el_pt": "AnalysisElectronsAuxDyn.pt",
    "el_eta": "AnalysisElectronsAuxDyn.eta",
    "el_phi": "AnalysisElectronsAuxDyn.phi",
    "el_charge": "AnalysisElectronsAuxDyn.charge",
    "mu_pt": "AnalysisMuonsAuxDyn.pt",
    "mu_eta": "AnalysisMuonsAuxDyn.eta",
    "mu_phi": "AnalysisMuonsAuxDyn.phi",
    "mu_charge": "AnalysisMuonsAuxDyn.charge",
    "eventNumber": "EventInfoAuxDyn.eventNumber",
    "jet_pt":"AnalysisJetsAuxDyn.pt",
    "jet_eta":"AnalysisJetsAuxDyn.eta",
    "jet_phi":"AnalysisJetsAuxDyn.phi",
    "jet_mass":"AnalysisJetsAuxDyn.m",
    "btag_prob":"BTagging_AntiKt4EMPFlowAuxDyn.DL1dv01_pb"
}
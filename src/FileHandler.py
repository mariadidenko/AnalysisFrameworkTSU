# AnalysisFramework/src/FileHandler.py

import uproot

def open_root_file(file_path):
    """
    Open the ROOT file and return the tree.
    """
    # Open the ROOT file using uproot
    file = uproot.open(file_path)
    
    # Access the tree by name (replace "AnalysisTree" with the correct tree name if necessary)
    tree = file["CollectionTree"]  # Modify this line if your tree has a different name
    
    return tree


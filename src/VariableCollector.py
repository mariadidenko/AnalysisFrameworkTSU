# AnalysisFramework/src/VariableCollector.py

import uproot3
import awkward as ak

def collect_variables(tree, branches):
    """Collect specified variables from the ROOT tree."""
    variables = {}
    
    for var_name, branch in branches.items():
        variables[var_name] = tree[branch].array()
    
    return variables
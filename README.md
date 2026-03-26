Main auto contingency script. Execute this to perform power flow contingency runs.

Instructions:
- Runs in command prompt, outside the PSS/e GUI.
- This script dumps the output in the .\out\ directory.

Dependencies:
- Basecases to run against are in the "autocont_runlist_basecase.py" list.
- Contingencies to run are in the "autocont_runlist_contingency.py" list.
- Contingency definitions are in the "autocont_defs_contingency.py" list.
- PSS/e .sav files must be inside the start directory.

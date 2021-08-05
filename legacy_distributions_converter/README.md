# PPSLegacyDistributionsConverter

Converts legacy (before 2018) distributions.root files to the new format. The main task is to adjust near_far/slice plots.

Example configuration of a cms process can be found in `run.converter.py`

The `PPSLegacyDistributionsConverter.cc` file implements a CMSSW EDAnalyzer, therefore it needs to be placed in CMSSW (e.g. in `CalibPPS/AlignmentGlobal/plugins`).

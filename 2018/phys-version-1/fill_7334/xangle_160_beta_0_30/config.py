import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.relpath(".."))

from config_fill import ppsAlignmentConfigESSource

ppsAlignmentConfigESSource.matching = cms.PSet(
    reference_datasets = cms.vstring(
        "../../../alig-version-3/fill_6554/xangle_160_beta_0_30/DQM_V0001_CalibPPS_R000314255.root"
    )
)

import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.relpath(".."))

from config_fill import ppsAlignmentConfigESSource

ppsAlignmentConfigESSource.sector_45.rp_N.slope = cms.double(0.18)
ppsAlignmentConfigESSource.sector_45.rp_F.slope = cms.double(0.17)
ppsAlignmentConfigESSource.sector_45.slope = cms.double(0.008)

ppsAlignmentConfigESSource.sector_56.rp_N.slope = cms.double(0.34)
ppsAlignmentConfigESSource.sector_56.rp_F.slope = cms.double(0.34)
ppsAlignmentConfigESSource.sector_56.slope = cms.double(-0.012)

ppsAlignmentConfigESSource.matching = cms.PSet(
    reference_datasets = cms.vstring(
        "../../../alig-version-3/fill_6554/xangle_130_beta_0_30/DQM_V0001_CalibPPS_R000314255.root"
    )
)
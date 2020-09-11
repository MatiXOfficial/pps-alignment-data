import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

from config_fill_ref import ppsAlignmentConfigESSource

ppsAlignmentConfigESSource.sector_45.cut_h_c = cms.double(0.04)
ppsAlignmentConfigESSource.sector_45.cut_v_c = cms.double(0.10)

ppsAlignmentConfigESSource.sector_56.cut_h_c = cms.double(0.26)
ppsAlignmentConfigESSource.sector_56.cut_v_c = cms.double(0.06)

ppsAlignmentConfigESSource.matching = cms.PSet(
    reference_dataset = cms.string(
        "../../../alig-version-3/fill_6554/xangle_160_beta_0_30/DQM_V0001_CalibPPS_R000314255.root"
    )
)
import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

from config_fill import ppsAlignmentConfigESSource

ppsAlignmentConfigESSource.sector_45.rp_N.slope = cms.double(0.155)
ppsAlignmentConfigESSource.sector_45.rp_F.slope = cms.double(0.140)

ppsAlignmentConfigESSource.sector_56.rp_N.slope = cms.double(0.210)
ppsAlignmentConfigESSource.sector_56.rp_F.slope = cms.double(0.210)

ppsAlignmentConfigESSource.matching = cms.PSet(
    reference_datasets = cms.vstring(
        "../../../alig-version-7/fill_6228/xangle_130_beta_0_30/distributions.root"
    )
)
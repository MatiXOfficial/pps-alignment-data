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
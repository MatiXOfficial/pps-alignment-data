import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

from config_period import ppsAlignmentConfigESSource

ppsAlignmentConfigESSource.sector_45.cut_h_c = cms.double(-38.56)
ppsAlignmentConfigESSource.sector_45.cut_v_c = cms.double(1.64)

ppsAlignmentConfigESSource.sector_56.cut_h_c = cms.double(-39.28)
ppsAlignmentConfigESSource.sector_56.cut_v_c = cms.double(1.49)
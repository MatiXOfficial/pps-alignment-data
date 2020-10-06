import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

from config_fill_ref import ppsAlignmentConfigESSource

ppsAlignmentConfigESSource.sector_45.cut_h_c = cms.double(0.04)
ppsAlignmentConfigESSource.sector_45.cut_v_c = cms.double(0.07)

ppsAlignmentConfigESSource.sector_56.cut_h_c = cms.double(0.19)
ppsAlignmentConfigESSource.sector_56.cut_v_c = cms.double(0.01)
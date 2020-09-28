import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.relpath("../../../alig-version-2/fill_5332/xangle_140_beta_0_40"))

from input_files import input_files
from config import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceTest
from config_reference import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceReference

process = cms.Process('testDistributions')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("DQMServices.Core.DQMStore_cfi")
process.load("CalibPPS.Alignment.ppsAlignmentHarvester_cfi")

process.MessageLogger = cms.Service("MessageLogger",
	destinations = cms.untracked.vstring(# 'run_analysis_manual', 
	                                     'cout'
	                                    ),
	# run_analysis_manual = cms.untracked.PSet(
	# 	threshold = cms.untracked.string("INFO")
	# ),
	cout = cms.untracked.PSet(
		threshold = cms.untracked.string('WARNING')
	)
)

# load DQM framework
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.dqmEnv.subSystemFolder = "CalibPPS"
process.dqmSaver.convention = 'Offline'
process.dqmSaver.workflow = "/CalibPPS/Alignment/CMSSW_11_2_0_pre2"
process.dqmSaver.saveByRun = 1

process.source = cms.Source("DQMRootSource",
	fileNames = cms.untracked.vstring(
		"file:dqm_run_distributions_test.root"
	),
)

process.ppsAlignmentConfigESSourceReference = ppsAlignmentConfigESSourceReference
process.ppsAlignmentConfigESSourceTest = ppsAlignmentConfigESSourceTest

process.path = cms.Path(
  	process.ppsAlignmentHarvester
)

process.end_path = cms.EndPath(
	process.dqmSaver
)

process.schedule = cms.Schedule(
	process.path,
	process.end_path
)
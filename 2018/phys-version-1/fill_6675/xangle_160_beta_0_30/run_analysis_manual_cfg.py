import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.relpath("../../../alig-version-3/fill_6554/xangle_160_beta_0_30"))

from config import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceTest
from config_reference import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceReference
ppsAlignmentConfigESSourceReference.matching = cms.PSet(
	reference_dataset = cms.string(
		"../../../alig-version-3/fill_6554/xangle_160_beta_0_30/DQM_V0001_CalibPPS_R000314255.root"
	)
)

process = cms.Process('testDistributions')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("DQMServices.Core.DQMStore_cfi")
process.load("CalibPPS.AlignmentGlobal.ppsAlignmentHarvester_cfi")

process.MessageLogger = cms.Service("MessageLogger",
	destinations = cms.untracked.vstring('run_analysis_manual', 
	                                     'cout'
	                                    ),
	run_analysis_manual = cms.untracked.PSet(
		threshold = cms.untracked.string("INFO")
	),
	cout = cms.untracked.PSet(
		threshold = cms.untracked.string('WARNING')
	)
)

# load DQM framework
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.dqmEnv.subSystemFolder = "CalibPPS"
process.dqmSaver.convention = 'Offline'
process.dqmSaver.workflow = "/CalibPPS/AlignmentGlobal/CMSSW_11_3_0_pre4"
process.dqmSaver.saveByRun = -1
process.dqmSaver.saveAtJobEnd = True
process.dqmSaver.forceRunNumber = 999999

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
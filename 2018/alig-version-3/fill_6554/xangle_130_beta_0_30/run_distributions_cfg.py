import FWCore.ParameterSet.Config as cms

from input_files import input_files
from config_reference import ppsAlignmentConfigESSource

process = cms.Process('referenceDistributions')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("CalibPPS.Alignment.ppsAlignmentWorkerReference_cfi")
process.load("DQMServices.Core.DQMStore_cfi")

# Message Logger
process.MessageLogger = cms.Service("MessageLogger",
	destinations = cms.untracked.vstring('run_distributions_log', 
	                                     'cout'
	                                    ),
	run_distributions_log = cms.untracked.PSet(
		threshold = cms.untracked.string("INFO")
	),
	cout = cms.untracked.PSet(
		threshold = cms.untracked.string('WARNING')
	)
)

# load DQM framework
process.load("DQM.Integration.config.environment_cfi")
process.dqmEnv.subSystemFolder = "CalibPPS"
process.dqmSaver.path = ""
process.dqmSaver.tag = "CalibPPS"

process.source = cms.Source("PoolSource",
	fileNames = input_files
)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(60000))

# Event Setup
process.ppsAlignmentConfigESSource = ppsAlignmentConfigESSource

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
	fileName = cms.untracked.string("dqm_run_distributions_reference.root")
)

process.path = cms.Path(
  	process.ppsAlignmentWorker
)

process.end_path = cms.EndPath(
	process.dqmEnv +
	process.dqmOutput +
	process.dqmSaver
)

process.schedule = cms.Schedule(
	process.path,
	process.end_path
)
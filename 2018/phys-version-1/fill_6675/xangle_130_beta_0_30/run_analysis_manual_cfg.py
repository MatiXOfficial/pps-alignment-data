import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.relpath("../../../alig-version-3/fill_6554/xangle_130_beta_0_30"))

from input_files import input_files
from config import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceTest
from config_reference import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceReference

process = cms.Process('testDistributions')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("DQMServices.Core.DQMStore_cfi")
process.load("CalibPPS.Alignment.ppsAlignmentHarvester_cfi")

process.MessageLogger = cms.Service("MessageLogger",
	destinations = cms.untracked.vstring('run_analysis_manual_out', 
	                                    #  'run_analysis_manual_log', 
	                                     'cout'
	                                    ),
	categories = cms.untracked.vstring('x_alignment_results',
	                                   'x_alignment_relative_results',
	                                   'y_alignment_results', 
	                                  ),
	run_analysis_manual_out = cms.untracked.PSet(
		threshold = cms.untracked.string("INFO"),
		INFO = cms.untracked.PSet(limit = cms.untracked.int32(0)),
		x_alignment_results = cms.untracked.PSet(limit = cms.untracked.int32(100000)),
		x_alignment_relative_results = cms.untracked.PSet(limit = cms.untracked.int32(100000)),
		y_alignment_results = cms.untracked.PSet(limit = cms.untracked.int32(100000))
	),
	# run_analysis_manual_log = cms.untracked.PSet(
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
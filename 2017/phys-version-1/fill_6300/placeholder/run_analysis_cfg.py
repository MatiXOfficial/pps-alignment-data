########## Configuration ##########
# if set to True, a file with logs will be produced.
produce_logs = True

# Path for a ROOT file with the histograms.
input_distributions = 'file:dqm_run_distributions_test.root'

# if set to True, the process will load the conditions input from an SQLite file. 
# Otherwise, it will use ESSource.
conditions_input_from_db = False  # test config
conditions_input_from_db_reference = False  # reference config

# Input database. Used only if conditions_input_from_db(_reference) is set to True.
input_conditions = 'sqlite_file:alignment_config.db'
input_conditions_reference = 'sqlite_file:../../../alig-version-3/fill_6554/xangle_160_beta_0_30/alignment_config_reference.db'

# Database tag. Used only if conditions_input_from_db(_reference) is set to True.
input_db_tag = 'PPSAlignmentConfig_test'
input_db_tag_reference = 'PPSAlignmentConfig_test'

# Reference dataset path. Only used if conditions_input_from_db_reference is set to False.
reference_dataset_path = '../../../alig-version-7/fill_6228/xangle_130_beta_0_30/new_distributions.root'

# If set to True, the results will be also written to an SQLite file.
write_sqlite_results = False

# Output database. Used only if write_sqlite_results is set to True.
output_conditions = 'sqlite_file:alignment_results.db'

# Database tag. Used only if write_sqlite_results is set to True.
output_db_tag = 'CTPPSRPAlignmentCorrectionsData_test'
###################################

import sys 
import os
import FWCore.ParameterSet.Config as cms

process = cms.Process('testDistributions')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("DQMServices.Core.DQMStore_cfi")
process.load("CalibPPS.AlignmentGlobal.ppsAlignmentHarvester_cfi")
process.ppsAlignmentHarvester.overwrite_sh_x = cms.bool(False)

process.ppsAlignmentHarvester.debug = cms.bool(True)

# Message Logger
if produce_logs:
    process.MessageLogger = cms.Service("MessageLogger",
        destinations = cms.untracked.vstring('run_analysis', 
                                            'cout'
                                            ),
        run_analysis = cms.untracked.PSet(
            threshold = cms.untracked.string("INFO")
        ),
        cout = cms.untracked.PSet(
            threshold = cms.untracked.string('WARNING')
        )
    )
else:
    process.MessageLogger = cms.Service("MessageLogger",
        destinations = cms.untracked.vstring('cout'),
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

# Source (histograms)
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring(input_distributions),
)

# Event Setup (test)
if not conditions_input_from_db:
    from config import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceTest
    process.ppsAlignmentConfigESSourceTest = ppsAlignmentConfigESSourceTest
else:
    process.load("CondCore.CondDB.CondDB_cfi")
    process.CondDB.connect = input_conditions
    process.PoolDBESSource = cms.ESSource("PoolDBESSource",
        process.CondDB,
        DumbStat = cms.untracked.bool(True),
        toGet = cms.VPSet(cms.PSet(
            record = cms.string('PPSAlignmentConfigRcd'),
            tag = cms.string(input_db_tag)
        )),
        appendToDataLabel = cms.string('')
    )

# Event Setup (reference)
if not conditions_input_from_db_reference:
    sys.path.append(os.path.relpath("../../../alig-version-7/fill_6228/xangle_130_beta_0_30"))
    from config_reference import ppsAlignmentConfigESSource as ppsAlignmentConfigESSourceReference
    ppsAlignmentConfigESSourceReference.matching = cms.PSet(
        reference_dataset = cms.string(reference_dataset_path)
    )
    process.ppsAlignmentConfigESSourceReference = ppsAlignmentConfigESSourceReference
else:
    process.load("CondCore.CondDB.CondDB_cfi")
    process.CondDB.connect = input_conditions_reference
    process.PoolDBESSourceReference = cms.ESSource("PoolDBESSource",
        process.CondDB,
        DumbStat = cms.untracked.bool(True),
        toGet = cms.VPSet(cms.PSet(
            record = cms.string('PPSAlignmentConfigRcd'),
            tag = cms.string(input_db_tag_reference)
        )),
        appendToDataLabel = cms.string('reference')
    )

# SQLite results
if write_sqlite_results:
    process.load("CondCore.CondDB.CondDB_cfi")
    process.CondDB.connect = output_conditions
    process.PoolDBOutputService = cms.Service("PoolDBOutputService",
        process.CondDB,
        timetype = cms.untracked.string('runnumber'),
        toPut = cms.VPSet(cms.PSet(
            record = cms.string('CTPPSRPAlignmentCorrectionsDataRcd'),
            tag = cms.string(output_db_tag)
        ))
    )

    # DB object maker parameters
    process.ppsAlignmentHarvester.write_sqlite_results = cms.bool(True)
    process.ppsAlignmentHarvester.record = cms.string('CTPPSRPAlignmentCorrectionsDataRcd')
    process.ppsAlignmentHarvester.SinceAppendMode = cms.bool(True)
    process.ppsAlignmentHarvester.Source = cms.PSet(IOVRun = cms.untracked.uint32(1))

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
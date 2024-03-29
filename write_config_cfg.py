########## Configuration ##########
output_conditions = 'sqlite_file:alignment_config.db'  # Output database.
run_number = 1  # beginning of the IOV
db_tag = 'PPSAlignmentConfig_v1_prompt'  # Database tag.
produce_logs = False  # if set to True, a file with logs will be produced.
product_instance_label = ''  # ES product label (empty for physics fill)
###################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("writePPSAlignmentConfig")

# Message Logger
if produce_logs:
    process.MessageLogger = cms.Service("MessageLogger",
        destinations = cms.untracked.vstring('write_config',
                                             'cout'
                                            ),
        write_config = cms.untracked.PSet(
            threshold = cms.untracked.string('INFO')
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

# Load CondDB service
process.load("CondCore.CondDB.CondDB_cfi")

# Output database (in this case local sqlite file)
process.CondDB.connect = output_conditions

# A data source must always be defined. We don't need it, so here's a dummy one.
process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(run_number),
    lastValue = cms.uint64(run_number),
    interval = cms.uint64(1)
)

# Output service
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDB,
    timetype = cms.untracked.string('runnumber'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('PPSAlignmentConfigRcd'),
        tag = cms.string(db_tag)
    ))
)

# ESSource
from config import ppsAlignmentConfigESSource
process.ppsAlignmentConfigESSource = ppsAlignmentConfigESSource

# DB object maker
process.config_writer = cms.EDAnalyzer("WritePPSAlignmentConfig",
    record = cms.string('PPSAlignmentConfigRcd'),
    loggingOn = cms.untracked.bool(True),
    SinceAppendMode = cms.bool(True),
    Source = cms.PSet(
        IOVRun = cms.untracked.uint32(1)
    ),
    label = cms.string(product_instance_label)  # product label
)

process.path = cms.Path(process.config_writer)

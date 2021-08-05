import FWCore.ParameterSet.Config as cms

process = cms.Process("distributionsConverter")

process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('cout'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    )
)

# A data source must always be defined. We don't need it, so here's a dummy one.
process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.converter = cms.EDAnalyzer("PPSLegacyDistributionsConverter")

process.path = cms.Path(process.converter)

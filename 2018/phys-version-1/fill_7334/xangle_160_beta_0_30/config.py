import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
    sequence = cms.vstring(
		"x alignment",
		"x alignment relative",
		"y alignment"
	),
)
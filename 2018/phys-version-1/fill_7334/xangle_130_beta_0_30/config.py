import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
    sequence = cms.vstring(
		# "x alignment",
		"x alignment relative",
		"y alignment"
	),

    sector_45 = cms.PSet(
        rp_N = cms.PSet(
            slope = cms.double(0.18)
        ),
        rp_F = cms.PSet(
            slope = cms.double(0.17)
        ),
        slope = cms.double(0.008)
    ),

    sector_56 = cms.PSet(
        rp_N = cms.PSet(
            slope = cms.double(0.34)
        ),
        rp_F = cms.PSet(
            slope = cms.double(0.34)
        ),
        slope = cms.double(-0.012),
    )
)
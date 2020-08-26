import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
    sequence = cms.vstring(
		# "x alignment",
		"x alignment relative",
		"y alignment"
	),

    sector_45 = cms.PSet(
        rp_N = cms.PSet(
            x_max_mode = cms.double(8.3)
        ),
        rp_F = cms.PSet(
            x_max_mode = cms.double(7.2)
        ),

        cut_h_c = cms.double(-38.55 + 0.35 - 0.08),
        cut_v_c = cms.double(1.63 - 0.20 + 0.25)
    ),

    sector_56 = cms.PSet(
        rp_N = cms.PSet(
            x_max_mode = cms.double(9.0)
        ),
        rp_F = cms.PSet(
            x_max_mode = cms.double(8.0)
        ),
        slope = cms.double(-0.012),

        cut_h_c = cms.double(-39.26 + 0.20),
        cut_v_c = cms.double(1.49 + 0.17)
    )
)
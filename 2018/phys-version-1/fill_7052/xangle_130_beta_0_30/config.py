import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
    sequence = cms.vstring(
		"x alignment",
		"x alignment relative",
		"y alignment"
	),

    sector_45 = cms.PSet(
        rp_N = cms.PSet(
            slope = cms.double(0.18),
            x_max_mode = cms.double(7.8)
        ),
        rp_F = cms.PSet(
            slope = cms.double(0.17),
            x_max_mode = cms.double(7.5)
        ),
        slope = cms.double(0.008),

        cut_h_c = cms.double(-38.55 + 0.5 - 0.08),
        cut_v_c = cms.double(1.63 - 1.15 + 0.25)
    ),

    sector_56 = cms.PSet(
        rp_N = cms.PSet(
            slope = cms.double(0.34),
            x_max_mode = cms.double(8.2)
        ),
        rp_F = cms.PSet(
            slope = cms.double(0.34),
            x_max_mode = cms.double(8.0)
        ),
        slope = cms.double(-0.012),

        cut_h_c = cms.double(-39.26 + 0.25),
        cut_v_c = cms.double(1.49 - 0.85)
    )
)
import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
    sequence = cms.vstring(
		"x_alignment",
		"x_alignment_relative",
		"y_alignment"
	),

    sector_45 = cms.PSet(
        rp_N = cms.PSet(
            x_max_fit_mode = cms.double(8.3),
            y_max_fit_mode = cms.double(8.3)
        ),
        rp_F = cms.PSet(
            x_max_fit_mode = cms.double(7.2),
            y_max_fit_mode = cms.double(7.2)
        ),

        cut_h_c = cms.double(-38.55 + 0.35 - 0.08),
        cut_v_c = cms.double(1.63 - 0.20 + 0.25)
    ),

    sector_56 = cms.PSet(
        rp_N = cms.PSet(
            x_max_fit_mode = cms.double(9.0),
            y_max_fit_mode = cms.double(9.0)
        ),
        rp_F = cms.PSet(
            x_max_fit_mode = cms.double(8.0),
            y_max_fit_mode = cms.double(8.0)
        ),

        cut_h_c = cms.double(-39.26 + 0.20),
        cut_v_c = cms.double(1.49 + 0.17)
    )
)
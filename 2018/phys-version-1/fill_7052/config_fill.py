import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
    sequence = cms.vstring(
		"x_alignment",
		"x_alignment_relative",
		"y_alignment"
	),

    sector_45 = cms.PSet(
        rp_N = cms.PSet(
            x_max_fit_mode = cms.double(7.8),
            y_max_fit_mode = cms.double(7.8)
        ),
        rp_F = cms.PSet(
            x_max_fit_mode = cms.double(7.5),
            y_max_fit_mode = cms.double(7.5)
        ),

        cut_h_c = cms.double(-38.55 + 0.5 - 0.08),
        cut_v_c = cms.double(1.63 - 1.15 + 0.25)
    ),

    sector_56 = cms.PSet(
        rp_N = cms.PSet(
            x_max_fit_mode = cms.double(8.2),
            y_max_fit_mode = cms.double(8.2)
        ),
        rp_F = cms.PSet(
            x_max_fit_mode = cms.double(8.0),
            y_max_fit_mode = cms.double(8.0)
        ),

        cut_h_c = cms.double(-39.26 + 0.25),
        cut_v_c = cms.double(1.49 - 0.85)
    )
)

ppsAlignmentConfigESSource.x_alignment_meth_o = cms.PSet(
    rp_L_N = cms.PSet(
        x_min = cms.double(13.5)
    )
)

ppsAlignmentConfigESSource.y_alignment = cms.PSet(
    rp_L_F = cms.PSet(
        x_min = cms.double(45.5)
    ),
    rp_L_N = cms.PSet(
        x_min = cms.double(7.8)
    ),
    rp_R_F = cms.PSet(
        x_min = cms.double(45.5)
    )
)
import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
	sector_45 = cms.PSet(
        rp_N = cms.PSet(
            x_max_fit_mode = cms.double(7.0),
            y_max_fit_mode = cms.double(7.0)
        ),
        rp_F = cms.PSet(
            x_max_fit_mode = cms.double(7.5),
            y_max_fit_mode = cms.double(7.5)
        ),

        cut_h_c = cms.double(-38.55 + 0.57 - 0.08),
        cut_v_c = cms.double(1.63 - 2.15 + 0.25)
    ),

    sector_56 = cms.PSet(
        rp_N = cms.PSet(
            x_max_fit_mode = cms.double(7.4),
            y_max_fit_mode = cms.double(7.4)
        ),
        rp_F = cms.PSet(
            x_max_fit_mode = cms.double(8.0),
            y_max_fit_mode = cms.double(8.0)
        ),

        cut_h_c = cms.double(-39.26 + 0.33),
        cut_v_c = cms.double(1.49 - 1.80)
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
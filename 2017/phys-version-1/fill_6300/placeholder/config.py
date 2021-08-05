import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
    sector_45 = cms.PSet(
        rp_N = cms.PSet(
            x_slice_min = cms.double(5.),
            x_slice_max = cms.double(14.),
            x_slice_w = cms.double(0.5),
            sh_x = cms.double(0.),
            slope = cms.double(0.18)
        ),
        rp_F = cms.PSet(
            x_slice_min = cms.double(5.),
            x_slice_max = cms.double(14.),
            x_slice_w = cms.double(0.5),
            sh_x = cms.double(0.),
            slope = cms.double(0.17)
        ),

        slope = cms.double(0.008),
        cut_h_c = cms.double(0),
        cut_v_c = cms.double(0) 
    ),

    sector_56 = cms.PSet(
        rp_N = cms.PSet(
            x_slice_min = cms.double(4.),
            x_slice_max = cms.double(13.),
            x_slice_w = cms.double(0.5),
            sh_x = cms.double(0.),
            slope = cms.double(0.34)
        ),
        rp_F = cms.PSet(
            x_slice_min = cms.double(4.),
            x_slice_max = cms.double(13.),
            x_slice_w = cms.double(0.5),
            sh_x = cms.double(0.),
            slope = cms.double(0.34)
        ),
        
        slope = cms.double(-0.012),
        cut_h_c = cms.double(0),
        cut_v_c = cms.double(0)
    ),

    min_RP_tracks_size = cms.uint32(0),
    max_RP_tracks_size = cms.uint32(2),

    matching = cms.PSet(
        rp_L_F = cms.PSet(
            sh_min = cms.double(-1.),
            sh_max = cms.double(1.),
        ),
        rp_L_N = cms.PSet(
            sh_min = cms.double(-1.),
            sh_max = cms.double(1.),
        ),
        rp_R_N = cms.PSet(
            sh_min = cms.double(-1.),
            sh_max = cms.double(1.),
        ),
        rp_R_F = cms.PSet(
            sh_min = cms.double(-1.),
            sh_max = cms.double(1.),
        ),
    ),

    x_alignment_meth_o = cms.PSet(
        rp_L_F = cms.PSet(
            x_min = cms.double(5.),
            x_max = cms.double(14.)
        ),
        rp_L_N = cms.PSet(
            x_min = cms.double(5.),
            x_max = cms.double(14.)
        ),
        rp_R_N = cms.PSet(
            x_min = cms.double(4.),
            x_max = cms.double(13.)
        ),
        rp_R_F = cms.PSet(
            x_min = cms.double(4.),
            x_max = cms.double(13.)
        ),
        fit_profile_min_bin_entries = cms.uint32(3),
        fit_profile_min_N_reasonable = cms.uint32(5)
    ),
    
    x_alignment_relative = cms.PSet(
        rp_L_N = cms.PSet(
            x_min = cms.double(6.),
            x_max = cms.double(13.)
        ),
        rp_R_N = cms.PSet(
            x_min = cms.double(4.25),
            x_max = cms.double(11.)
        )
    ),

    y_alignment = cms.PSet(
        rp_L_F = cms.PSet(
            x_min = cms.double(2.5),
            x_max = cms.double(5.5)
        ),
        rp_L_N = cms.PSet(
            x_min = cms.double(3.5),
            x_max = cms.double(6.5)
        ),
        rp_R_N = cms.PSet(
            x_min = cms.double(5.3),
            x_max = cms.double(9.5)
        ),
        rp_R_F = cms.PSet(
            x_min = cms.double(2.5),
            x_max = cms.double(5.5)
        ),
        mult_sel_proj_y_min_entries	= cms.uint32(5)
    ),

    binning = cms.PSet(
        pixel_x_offset = cms.double(0.),
        slice_n_bins_x = cms.uint32(20),
        slice_n_bins_y = cms.uint32(20)
    )
)
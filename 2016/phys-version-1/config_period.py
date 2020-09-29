import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
	sequence = cms.vstring(
		"x_alignment",
		"x_alignment_relative",
		"y_alignment"
	),
	
	sector_45 = cms.PSet(
		rp_N = cms.PSet(
			name = cms.string("L_1_N"),
			id = cms.int32(2),

			slope = cms.double(0.),
			sh_x = cms.double(-3.),

			x_min_fit_mode = cms.double(-2.),
			x_max_fit_mode = cms.double(3.),
			y_max_fit_mode = cms.double(10.),

			y_cen_add = cms.double(0.),

			x_slice_min = cms.double(7.),
			x_slice_max = cms.double(17.)
		),
		rp_F = cms.PSet(
			name = cms.string("L_1_F"),
			id = cms.int32(3),

			slope = cms.double(0.),
			sh_x = cms.double(-3.),

			x_min_fit_mode = cms.double(-2.),
			x_max_fit_mode = cms.double(3.),
			y_max_fit_mode = cms.double(10.),

			y_cen_add = cms.double(0.),

			x_slice_min = cms.double(7.),
			x_slice_max = cms.double(17.)
		),
		slope = cms.double(-0.008),

		cut_h_c = cms.double(-0.88),
		cut_v_a = cms.double(-1.13),
		cut_v_c = cms.double(-0.48),
	),

	sector_56 = cms.PSet(
		rp_N = cms.PSet(
			name = cms.string("R_1_N"),
			id = cms.int32(102),

			slope = cms.double(0.34),
			sh_x = cms.double(-3.),
			x_min_fit_mode = cms.double(-2.),
			x_max_fit_mode = cms.double(3.),
			y_max_fit_mode = cms.double(10.),

			y_cen_add = cms.double(0.),

			x_slice_min = cms.double(7.),
			x_slice_max = cms.double(19.)
		),
		rp_F = cms.PSet(
			name = cms.string("R_1_F"),
			id = cms.int32(103),

			slope = cms.double(0.),
			sh_x = cms.double(-3.),
			x_min_fit_mode = cms.double(-2.),
			x_max_fit_mode = cms.double(3.),
			y_max_fit_mode = cms.double(10.),

			y_cen_add = cms.double(0.),
			
			x_slice_min = cms.double(7.),
			x_slice_max = cms.double(19.)
		),
		slope = cms.double(0.),

		cut_h_apply = cms.bool(False),
		cut_h_c = cms.double(0.),
		cut_v_apply = cms.bool(False),
		cut_v_a = cms.double(-1.07),
		cut_v_c = cms.double(0.),
	),

	chiSqThreshold = cms.double(1000.),
	y_mode_unc_max_valid = cms.double(1.),
	y_mode_max_valid = cms.double(1.),

	x_alignment_meth_o = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(9.8),
			x_max = cms.double(16.)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(9.3),
			x_max = cms.double(15.)
		),
		rp_R_N = cms.PSet(
			x_min = cms.double(0.),
			x_max = cms.double(0.)
		),
		rp_R_F = cms.PSet(
			x_min = cms.double(5.),
			x_max = cms.double(15.)
		)
	),

	x_alignment_relative = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(9.5),
			x_max = cms.double(11.)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(9.5),
			x_max = cms.double(11.)
		),
		rp_R_N = cms.PSet(
			x_min = cms.double(0.),
			x_max = cms.double(0.)
		),
		rp_R_F = cms.PSet(
			x_min = cms.double(7.),
			x_max = cms.double(15.)
		)
	),

	y_alignment = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(7.5),
			x_max = cms.double(13.)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(7.5),
			x_max = cms.double(13.)
		),
		rp_R_N = cms.PSet(
			x_min = cms.double(0.),
			x_max = cms.double(0.)
		),
		rp_R_F = cms.PSet(
			x_min = cms.double(7.),
			x_max = cms.double(15.)
		)
	),

	binning = cms.PSet(
		pixel_x_offset = cms.double(0.)
	)
)
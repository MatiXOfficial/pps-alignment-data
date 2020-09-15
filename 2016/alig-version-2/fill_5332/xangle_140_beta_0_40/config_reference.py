import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
	debug = cms.bool(True),
	label = cms.string("reference"),

	sector_45 = cms.PSet(
		rp_N = cms.PSet(
			name = cms.string("L_1_N"),
			id = cms.int32(2),

			slope = cms.double(0.),
			sh_x = cms.double(-3.),

			y_cen_add = cms.double(-0.2),
			y_width_mult = cms.double(1.0),
			x_min_mode = cms.double(2.),
			x_max_mode = cms.double(10.)
		),
		rp_F = cms.PSet(
			name = cms.string("L_1_F"),
			id = cms.int32(3),

			slope = cms.double(0.),
			sh_x = cms.double(-3.),

			y_cen_add = cms.double(-0.2),
			y_width_mult = cms.double(1.0),
			x_min_mode = cms.double(2.),
			x_max_mode = cms.double(10.)
		),
		slope = cms.double(0.008),

		cut_h_c = cms.double(0.),
		cut_v_a = cms.double(-1.13),
		cut_v_c = cms.double(-0.48),

		nr_x_slice_min = cms.double(2.),
		nr_x_slice_max = cms.double(14.),
		fr_x_slice_min = cms.double(2.),
		fr_x_slice_max = cms.double(14.)
	),

	sector_56 = cms.PSet(
		rp_N = cms.PSet(
			name = cms.string("R_1_N"),
			id = cms.int32(102),

			slope = cms.double(0.34),
			sh_x = cms.double(-3.),

			y_cen_add = cms.double(-0.4),
			y_width_mult = cms.double(1.0),
			x_min_mode = cms.double(2.),
			x_max_mode = cms.double(10.)
		),
		rp_F = cms.PSet(
			name = cms.string("R_1_F"),
			id = cms.int32(103),

			slope = cms.double(0.),
			sh_x = cms.double(-3.),

			y_cen_add = cms.double(-0.4),
			y_width_mult = cms.double(1.0),
			x_min_mode = cms.double(2.),
			x_max_mode = cms.double(10.)
		),
		slope = cms.double(-0.012),

		cut_h_apply = cms.bool(False),
		cut_h_c = cms.double(0.),
		cut_v_apply = cms.bool(False),
		cut_v_a = cms.double(-1.07),
		cut_v_c = cms.double(0.),

		nr_x_slice_min = cms.double(7.),
		nr_x_slice_max = cms.double(19.),
		fr_x_slice_min = cms.double(7.),
		fr_x_slice_max = cms.double(19.)
	),

	chiSqThreshold = cms.double(1000.),
	y_mode_unc_max_valid = cms.double(1.),
	y_mode_max_valid = cms.double(1.),

	matching = cms.PSet(
		reference_dataset = cms.string('../../../alig-version-2/fill_5332/xangle_140_beta_0_40/distributions.root'),
		rp_L_F = cms.PSet(
			sh_min = cms.double(-5.5),
			sh_max = cms.double(-2.5)
		),
		rp_L_N = cms.PSet(
			sh_min = cms.double(-5.),
			sh_max = cms.double(-2.)
		),
		rp_R_N = cms.PSet(
			sh_min = cms.double(-5.),
			sh_max = cms.double(-2.)
		),
		rp_R_F = cms.PSet(
			sh_min = cms.double(-5.5),
			sh_max = cms.double(-2.5)
		)
	),

	x_alignment_meth_o = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(5.),
			x_max = cms.double(15.)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(6.),
			x_max = cms.double(15.)
		)
	),

	binning = cms.PSet(
		pixel_x_offset = cms.double(0.)
	)
)
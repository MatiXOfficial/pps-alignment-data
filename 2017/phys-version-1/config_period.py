import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
	sequence = cms.vstring(
		"x alignment",
		"x alignment relative",
		"y alignment"
	),

	sector_45 = cms.PSet(
		rp_N = cms.PSet(
			sh_x = cms.double(-3.45)
		),
		rp_F = cms.PSet(
			sh_x = cms.double(-42.05)
		),
		slope = cms.double(0.008),

		nr_x_slice_min = cms.double(6.5),
		nr_x_slice_max = cms.double(19.),
		fr_x_slice_min = cms.double(44.5),
		fr_x_slice_max = cms.double(58.)
	),

	sector_56 = cms.PSet(
		rp_N = cms.PSet(
			sh_x = cms.double(-2.5)
		),
		rp_F = cms.PSet(
			sh_x = cms.double(-42.1)
		),
		slope = cms.double(-0.012),

		nr_x_slice_min = cms.double(5.5),
		nr_x_slice_max = cms.double(17.),
		fr_x_slice_min = cms.double(44.5),
		fr_x_slice_max = cms.double(56.)
	),

	x_alignment_meth_o = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(49.),
			x_max = cms.double(57.)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(11.),
			x_max = cms.double(19.)
		),
		rp_R_N = cms.PSet(
			x_min = cms.double(7.),
			x_max = cms.double(15.)
		),
		rp_R_F = cms.PSet(
			x_min = cms.double(46.),
			x_max = cms.double(53.)
		)
	),

	x_alignment_relative = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(0.),
			x_max = cms.double(0.)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(8.),
			x_max = cms.double(10.)
		),
		rp_R_N = cms.PSet(
			x_min = cms.double(7.),
			x_max = cms.double(9.)
		),
		rp_R_F = cms.PSet(
			x_min = cms.double(0.),
			x_max = cms.double(0.)
		)
	),

	y_alignment = cms.PSet(
		rp_L_F = cms.PSet(
			x_min = cms.double(46.),
			x_max = cms.double(49.5)
		),
		rp_L_N = cms.PSet(
			x_min = cms.double(7.),
			x_max = cms.double(11.)
		),
		rp_R_N = cms.PSet(
			x_min = cms.double(6.),
			x_max = cms.double(10.)
		),
		rp_R_F = cms.PSet(
			x_min = cms.double(46.),
			x_max = cms.double(50.)
		)
	)    
)
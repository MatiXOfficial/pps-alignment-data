import FWCore.ParameterSet.Config as cms

ppsAlignmentConfigESSource = cms.ESSource("PPSAlignmentConfigESSource",
	label = cms.string('reference'),
	
	sector_45 = cms.PSet(
		rp_N = cms.PSet(
			y_cen_add = cms.double(-0.2),
			y_width_mult = cms.double(1.0)
		),
		rp_F = cms.PSet(
			y_cen_add = cms.double(-0.2),
			y_width_mult = cms.double(1.0)
		),
        cut_h_c = cms.double(0.04),
        cut_v_c = cms.double(0.07),
		nr_x_slice_min = cms.double(2.),
		nr_x_slice_max = cms.double(16.),
		fr_x_slice_min = cms.double(3.),
		fr_x_slice_max = cms.double(16.5)
	),

	sector_56 = cms.PSet(
		rp_N = cms.PSet(
			y_cen_add = cms.double(-0.4),
			y_width_mult = cms.double(1.0)
		),
		rp_F = cms.PSet(
			y_cen_add = cms.double(-0.4),
			y_width_mult = cms.double(1.0)
		),
        cut_h_c = cms.double(0.19),
        cut_v_c = cms.double(0.01),
		nr_x_slice_min = cms.double(2.),
		nr_x_slice_max = cms.double(16.),
		fr_x_slice_min = cms.double(2.5),
		fr_x_slice_max = cms.double(16.5)
	),

	x_alignment_meth_o = cms.PSet(
		rp_L_2_F = cms.PSet(
			x_min = cms.double(5.),
			x_max = cms.double(15.),
		),
		rp_L_1_F = cms.PSet(
			x_min = cms.double(5.),
			x_max = cms.double(15.),
		),
		rp_R_1_F = cms.PSet(
			x_min = cms.double(4.),
			x_max = cms.double(12.),
		),
		rp_R_2_F = cms.PSet(
			x_min = cms.double(4.),
			x_max = cms.double(12.),
		)
	),

	binning = cms.PSet(
		pixel_x_offset = cms.double(0.)
	)
)
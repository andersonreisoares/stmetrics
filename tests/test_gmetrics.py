"""Unit-test for stmetrics."""


def test_getmetrics():
	import numpy
	import stmetrics
	
	series = numpy.array([0.157327502966,0.168894290924,0.141409546137,
		                  0.113800831139,0.0922891944647,0.0747280195355,
		                  0.0537555813789,0.0660935789347,0.0770644843578,
		                  0.0739007592201,0.0983928665519,0.192401319742,
		                  0.286366194487,0.367539167404,0.420437157154,
		                  0.418041080236,0.413386583328,0.375436246395,
		                  0.335108757019,0.307270467281,0.250428706408,
		                  0,1,0,
		                  0.103006377816,0.115561470389,0.114221975207,
		                  0.172464296222,0.284338653088,0.386188000441,
		                  0.45704460144,0.571164608002,0.707974851131,
		                  0.648853778839,0.580699682236,0.566288888454,
		                  0.547502994537,0.500209212303,0.447707682848,
		                  0.39193546772,0.357513874769,0.290982276201,
		                  0.217830166221,0.148564651608,0.101060912013,
		                  0.111838668585,0.121473513544,0.113883294165,
		                  0.114351868629,0.116994164884,0.0982540994883,
		                  0.0843055993319,0.0827744230628,0.0758764594793,
		                  0.0936531722546,0.0942907482386,0.172556817532])

	metrics = {'basics': {'max_ts': 0.707974851131,
						  'min_ts': 0.0,
						  'mean_ts': 0.23782343004959103,
						  'std_ts': 0.18300599489659872,
						  'sum_ts': 13.318112082777098,
						  'amplitude_ts': 0.707974851131,
						  'mse_ts': 5.042865970724213,
						  'fslope_ts': 0.250428706408,
						  'skew_ts': 0.7958010591487271,
						  'amd_ts': 0.04354662597180001,
						  'abs_sum_ts': 13.318112082777098,
						  'iqr_ts': 0.280860923230625,
						  'fqr_ts': 0.09627242386345,
						  'tqr_ts': 0.38081212341799997,
						  'sqr_ts': 0.158729471266},
						 'polar': {'ecc_metric': 0.987689631116998,
						  'gyration_radius': 0.3783196562584793,
						  'area_ts': 0.276252576765137,
						  'polar_balance': 0.06904844444569475,
						  'angle': 3.54143171859213,
						  'area_q1': 0.04687908427114328,
						  'area_q2': 0.03317344409141949,
						  'area_q3': 0.1864297101292115,
						  'area_q4': 0.00977033827336271,
						  'csi': 2.6583365162722767,
						  'fill_rate': 0.08729895531064645,
						  'fill_rate2': 0.7010867703948551,
						  'symmetry_ts': 0.800411533476882},
						 'fractal': {'dfa_fd': 2.1012387123584535,
						  'hurst_exp': 0.8959523971291921,
						  'katz_fd': 1.427276909689125}}

	out = stmetrics.metrics.get_metrics(series,nodata=0.157327502966)
	assert metrics == out


def test_basics():

	import stmetrics
	import numpy

	basicas = {'max_ts': 1.0,
			   'min_ts': 1.0,
			   'mean_ts': 1.0,
			   'std_ts': 0.0,
			   'sum_ts': 360.0,
			   'amplitude_ts': 0.0,
			   'mse_ts': 360.0,
			   'fslope_ts': 0.0,
			   'skew_ts': 0.0,
			   'amd_ts': 0.0,
			   'abs_sum_ts': 360.0,
			   'iqr_ts': 0.0,
			   'fqr_ts': 1.0,
			   'tqr_ts': 1.0,
			   'sqr_ts': 1.0}

	bmetrics = stmetrics.basics.ts_basics(numpy.ones((1,360)).T)

	assert basicas == bmetrics

def test_fractal():
	
	import stmetrics
	import numpy

	fractais = {'dfa_fd': 0.750251960291734,
			    'hurst_exp': -1.4554390466381768,
			    'katz_fd': 1.0606600552401722}

	bmetrics = stmetrics.fractal.ts_fractal(numpy.ones((1,360)).T)

	assert fractais == bmetrics


def test_polares():
	
 	import stmetrics
 	import numpy

 	polares =  {'ecc_metric': 1.0,
				 'gyration_radius': 1.0,
				 'area_ts': 3.1414331587110302,
				 'polar_balance': 1.4686870114880517e-16,
				 'angle': 0.0,
				 'area_q1': 0.7853582896777579,
				 'area_q2': 0.785358289677758,
				 'area_q3': 0.7853582896777582,
				 'area_q4': 0.7853582896777582,
				 'csi': 1.000025385558271,
				 'fill_rate': 0.0,
				 'fill_rate2': -0.0007780634665712882,
				 'symmetry_ts': 0.0}

 	bmetrics = stmetrics.polar.ts_polar(numpy.ones((1,360)).T)

 	assert polares == bmetrics


def test_utils():
	import numpy
	import stmetrics
	
	series = numpy.array([0.157327502966,0.168894290924,0.141409546137,
		                  0.113800831139,0.0922891944647,0.0747280195355,
		                  0.0537555813789,0.0660935789347,0.0770644843578,
		                  0.0739007592201,0.0983928665519,0.192401319742,
		                  0.286366194487,0.367539167404,0.420437157154,
		                  0.418041080236,0.413386583328,0.375436246395,
		                  0.335108757019,0.307270467281,0.250428706408,
		                  0.178802281618,0.117247626185,0.11457183212,
		                  0.103006377816,0.115561470389,0.114221975207,
		                  0.172464296222,0.284338653088,0.386188000441,
		                  0.45704460144,0.571164608002,0.707974851131,
		                  0.648853778839,0.580699682236,0.566288888454,
		                  0.547502994537,0.500209212303,0.447707682848,
		                  0.39193546772,0.357513874769,0.290982276201,
		                  0.217830166221,0.148564651608,0.101060912013,
		                  0.111838668585,0.121473513544,0.113883294165,
		                  0.114351868629,0.116994164884,0.0982540994883,
		                  0.0843055993319,0.0827744230628,0.0758764594793,
		                  0.0936531722546,0.0942907482386,0.172556817532])	


	geometry = stmetrics.utils.create_polygon(series)

	if geometry.is_valid == True:
		pass


def test_polar():
	import numpy
	from stmetrics import utils

	polares = utils.error_polar()

	if all(numpy.isnan(value) != numpy.nan for value in polares.values()) == True:
		pass


def test_fractal():
	import numpy
	from stmetrics import utils
	fractal = utils.error_fractal()

	if all(numpy.isnan(value) != numpy.nan for value in fractal.values()) == True:
		pass


def test_basics():
	import numpy
	from stmetrics import utils
	basics = utils.error_basics()

	if all(numpy.isnan(value) != numpy.nan for value in basics.values()) == True:
		pass

def test_symmetric_distance():
	import numpy
	from stmetrics import polar

	s1 = numpy.ones((1,360)).T
	s2 = numpy.ones((1,360)).T

	dist = polar.symmetric_distance(s1, s2)

	assert dist == 0

def test_symmetric_distance_ii():
	import numpy
	from stmetrics import polar

	s1 = numpy.ones((1,360)).T-0.1
	s2 = numpy.ones((1,360)).T

	dist = polar.symmetric_distance(s1, s2)

	assert dist == 0.596872300155098

def test_geometries():

	from shapely import geometry
	from stmetrics import spatial

	p1 = geometry.Point(0,0)
	p2 = geometry.Point(1,0)
	p3 = geometry.Point(1,1)
	p4 = geometry.Point(0,1)

	pointList = [p1, p2, p3, p4, p1]

	poly = geometry.Polygon([[p.x, p.y] for p in pointList])

	out = [0.0, 1.0, 0.6376435773361453, 0.0, 1.0, 1.0]

	res = [spatial.symmetry(poly),
		   spatial.aspect_ratio(poly),
	 	   spatial.reock_compactness(poly),
	 	   spatial.rectangular_fit(poly),
	 	   spatial.width(poly),
		   spatial.length(poly)]

	assert out == res


def test_getmetrics_sits():
    import numpy
    from stmetrics import metrics

    out = numpy.array([ 1.00000000e+00,  1.00000000e+00,  1.00000000e+00,  0.00000000e+00,
        3.60000000e+02,  0.00000000e+00,  3.60000000e+02,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  3.60000000e+02,  0.00000000e+00,
        1.00000000e+00,  1.00000000e+00,  1.00000000e+00,  1.00000000e+00,
        1.00000000e+00,  3.14143316e+00,  1.46868701e-16,  0.00000000e+00,
        7.85358290e-01,  7.85358290e-01,  7.85358290e-01,  7.85358290e-01,
        1.00002539e+00,  0.00000000e+00, -7.78063467e-04,  0.00000000e+00,
        7.50251960e-01,  1.17661310e+00,  1.06066006e+00])

    assert all(numpy.round(out) == numpy.round(metrics._getmetrics(numpy.ones((1,360)).T)))

def test_list_metrics():
	from stmetrics import utils
	out = ['max_ts',
		 'min_ts',
		 'mean_ts',
		 'std_ts',
		 'sum_ts',
		 'amplitude_ts',
		 'mse_ts',
		 'fslope_ts',
		 'skew_ts',
		 'amd_ts',
		 'abs_sum_ts',
		 'iqr_ts',
		 'fqr_ts',
		 'tqr_ts',
		 'sqr_ts',
		 'ecc_metric',
		 'gyration_radius',
		 'area_ts',
		 'polar_balance',
		 'angle',
		 'area_q1',
		 'area_q2',
		 'area_q3',
		 'area_q4',
		 'fill_rate',
		 'csi',
		 'fill_rate2',
		 'symmetry_ts',
		 'dfa_fd',
		 'hurst_exp',
		 'katz_fd']

	assert all([out == utils.list_metrics()])


def test_sits2metrics_exception():
	import numpy
	import stmetrics
	import pytest

	with pytest.raises(Exception):
		assert stmetrics.metrics.sits2metrics([10])


def test_create_polygon_exception():
	import stmetrics
	import pytest

	with pytest.raises(Exception):
		assert stmetrics.utils.create_polygon([10])


def test_check_input_exception():
	import stmetrics
	import pytest

	with pytest.raises(Exception):
		assert stmetrics.utils.check_input([10])

 
def test_sits2metrics():

	import numpy
	import stmetrics

	sits = numpy.array([[[0.08213558, 0.58803765],
				        [0.49712389, 0.83526625]],

				       [[0.88548059, 0.30089922],
				        [0.46782818, 0.84561955]],

				       [[0.97508056, 0.37090787],
				        [0.23905704, 0.96134861]],

				       [[0.34126892, 0.0517639 ],
				        [0.56801062, 0.9046814 ]],

				       [[0.89621465, 0.79039706],
				        [0.76447722, 0.37223732]],

				       [[0.01181458, 0.92984248],
				        [0.95011783, 0.94595306]],

				       [[0.19884843, 0.86591456],
				        [0.25220217, 0.54905   ]],

				       [[0.44872961, 0.61002462],
				        [0.43320113, 0.41983541]],

				       [[0.67116755, 0.70299412],
				        [0.06319867, 0.99832697]],

				       [[0.57694712, 0.30948048],
				        [0.9029195 , 0.99803176]]])

	output = numpy.array([[[ 0.97508056,  0.92984248],
				        [ 0.95011783,  0.99832697]],

				       [[ 0.01181458,  0.0517639 ],
				        [ 0.06319867,  0.37223732]],

				       [[ 0.50876876,  0.5520262 ],
				        [ 0.51381363,  0.78303503]],

				       [[ 0.33123788,  0.2702782 ],
				        [ 0.27629901,  0.22973304]],

				       [[ 5.08768759,  5.52026196],
				        [ 5.13813625,  7.83035033]],

				       [[ 0.96326598,  0.87807858],
				        [ 0.88691916,  0.62608965]],

				       [[ 3.68564181,  3.77783228],
				        [ 3.40345586,  6.65921134]],

				       [[ 0.88440007,  0.73863316],
				        [ 0.83972083,  0.57849156]],

				       [[-0.04801069, -0.29963436],
				        [ 0.12850238, -0.80783331]],

				       [[ 0.41329731,  0.26229674],
				        [ 0.33975173,  0.26597931]],

				       [[ 5.08768759,  5.52026196],
				        [ 5.13813625,  7.83035033]],

				       [[ 0.59744878,  0.443709  ],
				        [ 0.41790866,  0.33689566]],

				       [[ 0.27005867,  0.34019417],
				        [ 0.34270165,  0.69215812]],

				       [[ 0.77832407,  0.74669559],
				        [ 0.66624392,  0.95365084]],

				       [[ 0.51283837,  0.59903113],
				        [ 0.48247604,  0.87515047]],

				       [[ 0.95581025,  0.7489213 ],
				        [ 0.78054901,  0.97963461]],

				       [[ 0.17676586,  0.85565149],
				        [ 0.6298049 ,  0.67398157]],

				       [[ 0.70907914,  0.95379636],
				        [ 0.74147572,  1.78594009]],

				       [[ 0.10687003,  0.13229527],
				        [ 0.10727764,  0.1576635 ]],

				       [[ 1.3962634 ,  3.4906585 ],
				        [ 3.4906585 ,  5.58505361]],

				       [[ 0.11835326,  0.22871022],
				        [ 0.36917054,  0.3263756 ]],

				       [[ 0.34756873,  0.08975312],
				        [ 0.113039  ,  0.57817949]],

				       [[ 0.06238014,  0.4504295 ],
				        [ 0.10955383,  0.25685248]],

				       [[ 0.18077701,  0.18490352],
				        [ 0.14971235,  0.62453252]],

				       [[ 3.37237834,  1.76130242],
				        [ 2.54367407,  1.50849323]],

				       [[ 0.59671668,  0.22800158],
				        [ 0.30856437,  0.31000387]],

				       [[ 0.61580575,  0.47960716],
				        [ 0.58494611,  0.27282604]],

				       [[ 3.65164699,  7.21850635],
				        [ 3.1097162 ,  7.33601293]],

				       [[-0.3501718 , -0.15126148],
				        [ 1.08772094,  0.04505297]],

				       [[ 0.60123181,  0.60001261],
				        [ 0.72512761,  0.75648882]],

				       [[ 1.73692591,  1.63311368],
				        [ 1.94143426,  1.4991057 ]]])

	res = stmetrics.metrics.sits2metrics(sits)

	r1 = res.reshape(res.shape[0]*res.shape[1]*res.shape[2])
	r2 = output.reshape(output.shape[0]*output.shape[1]*output.shape[2])

	assert all(numpy.round(r1) == numpy.round(r2))


if __name__ == '__main__':
    pytest.main(['--color=auto', '--no-cov'])
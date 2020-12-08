import numpy
from .utils import fixseries, truncate


def ts_fractal(timeseries, funcs=['all'], nodata=-9999):
    """This function compute 4 fractal dimensions and the hurst exponential.

        - DFA: measures the Hurst parameter H, which is very similar to the \
        Hurst exponent.
        - HE: self-similarity measure that assess long-range dependence in a \
        time series.
        - KFD: This algorirhm computes the FD using Katz algorithm.

    :param timeseries: Time series.
    :type timeseries: numpy.ndarray

    :param nodata: nodata of the time series. Default is -9999.
    :type nodata: int

    :return out_metrics: Array of fractal metrics values
    """
    out_metrics = dict()

    if "all" in funcs:
        funcs = [
                'dfa_fd',
                'hurst_exp',
                'katz_fd'
                ]

    for f in funcs:
        try:
            out_metrics[f] = eval(f)(timeseries)
        except:
            out_metrics[f] = numpy.nan

    return out_metrics


def dfa_fd(timeseries):
    """dfa_fd - Detrended Fluctuation Analysis (DFA) - Measures the Hurst \
    parameter H, which is very similar to the Hurst exponent.

    The main difference is that DFA can be used for non-stationary \
    time series.

    :param timeseries: Time series.
    :type timeseries: numpy.ndarray

    :return dfa: Detrended Fluctuation Analysis.
    .. Note::
        This functions uses the dfa implementation from the Nolds package.
    """
    import nolds
    ts = fixseries(timeseries)

    return truncate(nolds.dfa(ts))
    

def hurst_exp(timeseries):
    """hurst_exp - Hurst exponent - Computes the H exponent by a standard \
    rescaled range (R/S) approach.

    Hurst exponent is a self-similarity measure that assess long-range \
    dependence in a time series. It can be used to determine whether the \
    time series is more, less, or equally likely to increase if it has \
    increased in previous steps.

    :param timeseries: Time series.
    :type timeseries: numpy.ndarray

    :return hurst: Hurst expoent.

    .. Note::
        This function was adapted from the package Nolds.
    """
    import nolds
    ts = fixseries(timeseries)

    return truncate(nolds.hurst_rs(ts))


def katz_fd(timeseries):
    """katz_fd - Katz fractal dimension - Computes Katz fractal dimension.

    It is defined by:

    .. math:: K = \\frac{\\log_{10}(n)}{\\log_{10}(d/L)+\\log_{10}(n)}

    where :math:`L` is the total length of the time series and :math:`d` \
    is the Euclidean distancebetween the first point in the series and \
    the point that provides the furthest distance with respect to \
    the first point.

    :param timeseries: Time series.
    :type timeseries: numpy.ndarray

    :return kfd: Katz fractal dimension.

    .. Note::
        This function was adapted from the package entropy available \
        at: https://github.com/raphaelvallat/entropy.

    .. Tip:: To know more about it:

        Michael J. Katz, Fractals and the analysis of waveforms, \
        Computers in Biology and Medicine, volume 18, Issue 3,1988,\
        Pages 145-156,ISSN 0010-4825,\
        https://doi.org/10.1016/0010-4825(88)90041-8.

        Esteller, R. et al. (2001). A comparison of waveform fractal dimension\
        algorithms. IEEE Transactions on Circuits and Systems I: Fundamental \
        Theory and Applications, 48(2), 177-183.

        Goh, Cindy, et al. "Comparison of fractal dimension algorithms for the\
        computation of EEG biomarkers for dementia." 2nd International \
        Conference on Computational Intelligence in Medicine and Healthcare \
        (CIMED2005). 2005.
    """
    ts = fixseries(timeseries)

    # absolute differences between consecutive elements of an array
    dists = numpy.abs(numpy.ediff1d(ts))
    # sum distances
    d_sum = dists.sum()
    # compute ln using the accumulated distance and the average distance
    ln = numpy.log10(numpy.divide(d_sum, dists.mean()))
    # define box limit
    d = numpy.max(ts) - numpy.min(ts)
    ln_sum = numpy.add(ln, numpy.log10(numpy.divide(d, d_sum)))
    # return katz fractal dimension
    return truncate(numpy.divide(ln, ln_sum))

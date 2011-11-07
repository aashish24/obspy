# -*- coding: utf-8 -*-
"""
Various utilities for ObsPy.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""

# import order matters - NamedTemporaryFile must be one of the first!
from obspy.core.util.attribdict import AttribDict
from obspy.core.util.base import NamedTemporaryFile, add_doctests, \
    add_unittests, ALL_MODULES, DEFAULT_MODULES, NATIVE_BYTEORDER, \
    WAVEFORM_PREFERRED_ORDER, c_file_p, createEmptyDataChunk, getEntryPoints, \
    getExampleFile, getMatplotlibVersion, _getPlugins, _getVersionString
from obspy.core.util.decorator import deprecated, deprecated_keywords, \
    interceptDict, skip, skipIf, uncompressFile
from obspy.core.util.geodetics import calcVincentyInverse, gps2DistAzimuth
from obspy.core.util.misc import BAND_CODE, complexifyString, guessDelta, \
    formatScientific, scoreatpercentile

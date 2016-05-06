# -*- coding: utf-8 -*-
"""
Exceptions for FlyingCircus.
"""


class FlyingCircusException(Exception):
    """
    Base exception class for FlyingCircus.
    """
    def __str__(self):
        return self.message


class UnnamedDataError(FlyingCircusException):
    """
    An exception raised when a parameter is loaded without a name.

    :param filename: The name of the file from which the data was loaded.
    :type filename: str
    """
    def __init__(self, filename):
        self.filename = filename
        self.message = 'Data read from "%s" without names.' % self.filename


class PVSimTimezoneError(FlyingCircusException):
    """
    An exception raised when PVSim timezone is in unexpected format.

    :param timezone: The timezone string that was read from the PVSim file.
    :type timezone: str
    """
    def __init__(self, timezone):
        self.timezone = timezone
        self.message = 'Incorrect timezone format: "%s".' % self.timezone


class DuplicateRegItemError(FlyingCircusException):
    """
    An exception raised when duplicate data is registered.

    :param keys: Keys of the duplicate data.
    :type keys: set
    """
    def __init__(self, keys):
        self.duplicate_keys = keys
        self.message = ('Duplicate data can\'t be registered:\n\t%s' %
                        '\n\t'.join(self.duplicate_keys))


class MismatchRegMetaKeysError(FlyingCircusException):
    """
    An exception raised when meta with mismatched keys is registered.

    :param keys: Keys of the mismatched meta.
    :type keys: set
    """
    def __init__(self, keys):
        self.mismatch_keys = keys
        self.message = ('Meta must be a subset of registry:\n\t%s' %
                        '\n\t'.join(self.mismatch_keys))


class UncertaintyPercentUnitsError(FlyingCircusException):
    """
    An exception raised when uncertainty doesn't have percent units.

    :param key: Key of uncertainty that doesn't have percent units.
    :type key: str
    :param units: Units of the uncertainty key that doesn't have percent units.
    :type units: str
    """
    def __init__(self, key, units):
        self.data_key = key
        self.units = units
        self.message = (
            'Uncertainty can only have units of percent (%%), but "%s" ' +
            'has units of "%s" instead.'
        ) % (self.data_key, self.units)


class UncertaintyBoundsUnitsError(FlyingCircusException):
    """
    An exception raised when the lower and upper uncertainty bounds do not have
    matching units, which should both be percent, otherwise
    :exc:`UncertaintyPercentUnitsError` is raised.

    :param key: Uncertainty key with mismatched lower and upper bounds.
    :type key: str
    :param lo_units: Units of lower uncertainty bound.
    :type lo_units: :mod:`quantities`
    :param up_units: Units of upper uncertainty bound
    :type up_units: :mod:`quantities`
    """
    def __init__(self, key, lo_units, up_units):
        self.data_key = key
        self.lo_units = lo_units.dimensionality
        self.up_units = up_units.dimensionality
        self.message = (
            'Uncertainty lower and upper bounds must both have units of ' +
            'percent (%%), but "%s" has units of "%s" for the lower bound ' +
            'and "%s" for the upper bound.'
        ) % (self.data_key, self.lo_units, self.up_units)


class CircularDependencyError(Exception):
    """
    Topological sort cyclic error.
    """
    def __init__(self, keys):
        self.calc = keys
        self.message = 'Not a DAG. Cyclic keys:\n\t%s' % '\n\t'.join(self.calc)


class MixedTextNoMatchError(Exception):
    """
    No match in mixed text data source error.
    """
    def __init__(self, re_meth, pattern, data):
        self.re_meth = re_meth
        self.pattern = pattern
        self.data = data
        self.message = ('No match using regex "%s" with "%s" in "%s".' %
                        (self.re_meth, self.pattern, self.data))

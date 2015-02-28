"""
@file
@brief Defines @see cl SkLearnParameters
"""

class SkException (Exception):
    """
    custom exception
    """
    pass

class SkLearnParameters:
    """
    defines a container for the parameters in a custom scikit learner
    """
    def __init__(self, **kwargs):
        """
        constructor, stores the parameters
        """
        self._keys = list(kwargs.keys())
        for k,v in kwargs.items():
            self.validate(k, v)
            setattr(self, k, v)

    def validate(self, name, value):
        """
        validates a parameter name and value

        @param  name        parameter name
        @param  value       parameter value
        @raises             @see cl SkException if something is wrong
        """
        if name.startswith("_") or name.endswith("_"):
            raise SkException("a parameter cannot begin or end with _: {0}".format(name))

    @property
    def Keys(self):
        """
        returns keys
        """
        return self._keys

    def __str__(self):
        """
        usual
        """
        def fmt(v):
            if isinstance(v, str): return "'{0}'".format(v)
            else: return str(v)
        return ", ".join( "{0}={1}".format(k,fmt(getattr(self,v))) for k in sorted(self.Keys) )

    def to_dict(self):
        """
        returns the parameters as a dictionary

        @return         dict
        """
        return { k:getattr(self,k) for k in self.Keys }
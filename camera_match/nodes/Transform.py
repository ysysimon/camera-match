from colour import cctf_decoding, cctf_encoding, RGB_to_RGB

class CST:
    def __init__(self, source_gamma=None, target_gamma=None, source_colourspace=None, target_colourspace=None):
        """
        Convert RGB array from one colourspace to another
        similar to Resolve's Color Space Transform.

        Note: Gamma values set to None are equivalent to
        "Linear" gamma in Resolve.
        """

        self.source_gamma = source_gamma
        self.target_gamma = target_gamma
        self.source_colourspace = source_colourspace
        self.target_colourspace = target_colourspace

    def apply(self, RGB):
        """
        Applies Color Space Transform to an RGB array.
        """

        if self.source_gamma is not None:
            RGB = cctf_decoding(RGB, function=self.source_gamma)

        if self.source_colourspace is not None and self.target_colourspace is not None:
            RGB = RGB_to_RGB(RGB, self.source_colourspace, self.target_colourspace)

        if self.target_gamma is not None:
            RGB = cctf_encoding(RGB, function=self.target_gamma)

        return RGB

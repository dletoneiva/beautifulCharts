class Chart: 
    def __init__(self):
        """
        Initializes the chart object with default values.

        Attributes:

            primaryColorPalette (list of 5 hex): list containing the primary 
            color palette (RGB)

            secondaryColorPalette (list of 4 hex): list containing the secondary 
            color palette (RGB)
        """
        self.primaryColorPalette = ['#DB6B2E',
                                    '#E28958',
                                    '#E9A682',
                                    '#F1C4AB',
                                    '#F8E1D5'] # set in orange colors
        
        self.secondaryColorPalette = ['#CF3779',
                                      '#ADC242',
                                      '#432466',
                                      '#55A8B5'] # set in happy colors

    def changeColorPalettePrimary(self, color_palette):
        """
        Changes the primary color palette, low conspicuity uses

        Args:
            color_palette: list of 5 hex codes for RGB
        
        Returns:
            None

        """
        if len(color_palette)!= 5:
            return 'Incompatible list size.'
        else:
            self.primaryColorPalette = color_palette
            return self.primaryColorPalette
        

    def changeColorPaletteSecondary(self, color_palette):
        """
        Changes the secondary color palette, high conspicuity uses

        Args:
            color_palette: list of 4 hex codes for RGB
        
        Returns:
            None

        """
        pass
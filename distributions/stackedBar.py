import matplotlib.pyplot as plt
from .BeautifulChart import Chart

class stackedBar(Chart):
    """
    Plots a stacked bar pattern for the data. Better used for part-all
    comparisons (like how a team behaves compared to the overall company).

    Attributes:
        localValues (float): array of values to be plotted (local)
        overallValues (float): array of values to be plotted in the overall view
        categories (string): array of strings containing categories
    """
    def __init__(self, localValues, overallValues, categories):

        self.localValues = localValues
        self.overallValues = overallValues
        self.categories = categories
        
        Chart.__init__(self)
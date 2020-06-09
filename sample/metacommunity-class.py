class Metacommunity:
    """A Metacommunity class object."""
    # define method
    def __init__(self, species, type_abundance, similarity, ordinariness, subcommunity_weights, type_weights):    
        # define attributes
        self.species = species
        self.type_abundance = type_abundance
        self.similarity = similarity
        self.ordinariness = ordinariness
        self.subcommunity_weights = subcommunity_weights
        self.type_weights = type_weights
    
    def raw_alpha(self):
        return 1 / ordinariness
        
    def norm_alpha(self):
        ordinariness_bar = np.divide(ordinariness,subcommunity_weights)
        return 1 / ordinariness_bar

    def raw_rho(self):
        return np.divide(ordinariness.sum(axis=1),ordinariness)

    def norm_rho(self):
        ordinariness_bar = np.divide(ordinariness,subcommunity_weights)
        return np.divide(ordinariness.sum(axis=1),ordinariness_bar)

    def raw_beta(self):
        return 1 / np.divide(ordinariness.sum(axis=1), ordinariness)

    def norm_beta(self):
        ordinariness_bar = np.divide(ordinariness, subcommunity_weights)
        normrho = np.divide(ordinariness.sum(axis=1), ordinariness_bar)
        return 1 / normrho
        
    def raw_gamma(self):
        return 1 / ordinariness.sum(axis=1)

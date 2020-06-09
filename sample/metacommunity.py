def metacommunity(partition, similarity=None):
    """Return metacommunity object.
    partition -- pandas dataframe, with first column 'species'
    """
    species = partition.species 
    S = len(species)
    abundances = partition.drop(columns='species')
    type_abundance = abundances / abundances.to_numpy().sum()
    subcommunity_weights = type_abundance.sum(axis=0)
    type_weights = type_abundance.sum(axis=1)
    
    if similarity is None:
        similarity = np.identity(S)
    ordinariness = np.matmul(similarity, type_abundance)
    
    results = Metacommunity(species, type_abundance, similarity, ordinariness, subcommunity_weights, type_weights)
    return results



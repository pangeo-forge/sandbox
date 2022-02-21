# ## Imports

# +
# import pandas as pd

from pangeo_forge_recipes.recipes import XarrayZarrRecipe
# from pangeo_forge_recipes.recipes import HDFReferenceRecipe
from pangeo_forge_recipes.patterns import ConcatDim, FilePattern, MergeDim


# -

# ## URL Format Function

# +
def make_url(time):
    base_url = "https://data-provider.org/dataset"
    generalized_filepath = "{time}.nc"
    return f"{base_url}/{generalized_filepath.format(time=time)}"

# def make_url(time, variable):
#    base_url = "https://data-provider.org/dataset"
#    generalized_filepath = "{time}-{variable}.nc"
#    return f"{base_url}/{generalized_filepath.format(time=time, variable=variable)}"
# -

# ## Combine Dims

# +
dates = pd.date_range("1990-01-01", "2021-01-01", freq="M")
concat_dim = ConcatDim(
    "time",
    keys=dates,
    # ninputs_per_file=10,
)

# variables = ["temperature", "salinity"]
# merge_dim = MergeDim("variable", keys=variables)
# -

# ## Define `FilePattern`

# +
pattern = FilePattern(make_url, concat_dim)

# pattern = FilePattern(make_url, concat_dim, merge_dim)
# -

# ## Define recipe

recipe = XarrayZarrRecipe(
    pattern,
    # target_chunks = {"time": 10},
)

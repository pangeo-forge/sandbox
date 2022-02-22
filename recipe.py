# # WELCOME!
# We're so glad you've found the Pangeo Forge Sandbox, a place to design your own Pangeo Forge Recipe.
#
#   1. This file is designed to be run on Binder in a purpose-built JupyterHub environment.
#      If you are _not_ reading this there, please go to https://github.com/pangeo-forge/sandbox
#      and click the _**launch binder**_ link in the README before proceeding.
#   2. If you are already on Binder, and reading this document as plain text, please right-click the
#      `recipe.py` file in the file browser on the lefthand side of the screen, and select
#      **Open With > Notebook**.
#   3. Awesome! You should now be reading this file as a Jupyter Notebook.
#
# > Note: If you're having trouble with any of the above steps, check to see if your issue is already listed
# > on https://github.com/pangeo-forge/sandbox/issues. If not, please open a new Issue describing your problem.

# ## STEP 1: IMPORTS
#
# In this first section, import `pangeo-forge-recipes` components along with any third party libraries you might need.
# The imports provided are suggestions; feel free to adjust as needed.

# +
import pandas as pd

from pangeo_forge_recipes.patterns import ConcatDim, FilePattern, MergeDim
from pangeo_forge_recipes.recipes import XarrayZarrRecipe


# -

# ## STEP 2: URL FORMAT FUNCTION
#
# Next, define a function which returns URLs for your dataset.
# Choose from one of the template options, depending on the structure of your source data.

# +
# ---- Option 2.1: Concatenating only ------- 

def make_url(time):
    base_url = "https://data-provider.org/dataset"
    generalized_filepath = "{time:%Y-%m-%d}.nc"
    return f"{base_url}/{generalized_filepath.format(time=time)}"

# ---- Option 2.2: Concatenating & merging ---

# def make_url(time, variable):
#     base_url = "https://data-provider.org/dataset"
#     generalized_filepath = "{time:%Y-%m-%d}-{variable}.nc"
#     return f"{base_url}/{generalized_filepath.format(time=time, variable=variable)}"
# -

# ## STEP 3: COMBINE DIMS

# +

# ---- Option 3.1: Concatenating only ------- 

dates = pd.date_range("1990-01-01", "2022-01-01", freq="D")

concat_dim = ConcatDim(
    "time",
    keys=dates,
    # nitems_per_file=10,
)

# ---- Option 3.2: Concatenating & merging ---

# variables = ["temperature", "salinity"]
# merge_dim = MergeDim("variable", keys=variables)
# -

# ## STEP 4: FILE PATTERN

# +
# ---- Option 4.1: Concatenating only ------- 

pattern = FilePattern(make_url, concat_dim)

# ---- Option 4.2: Concatenating & merging ---

# pattern = FilePattern(make_url, concat_dim, merge_dim)
# -

# #### INTERLUDE: INSPECT FILE PATTERN

# +
# from rich import print

# for i, (index, url) in enumerate(pattern.items()):
#     if i < 3 or i > (len(dates) - 4):
#         print(repr(index), url)
# -

# ## STEP 5: DEFINE RECIPE

recipe = XarrayZarrRecipe(
    pattern,
    target_chunks = {"time": 10},
)

# #### POSTSCRIPT: EXECUTE RECIPE SUBSET

# +
# from pangeo_forge_recipes.recipes import setup_logging

# setup_logging()

# pruned_recipe = recipe.copy_pruned()

# pruned_recipe.to_function()()

# +
# import xarray as xr

# ds = xr.open_zarr(pruned_recipe.target_mapper)
# ds
# -

# # NEXT STEPS
#
#   1. Customize your `meta.yaml`. A template is provided in the file browser on the lefthand side of your screen.
#   2. Submit your `recipe.py` and `meta.yaml` together as a Pull Request (PR) to https://github.com/pangeo-forge/staged-recipes
#      For more detail on how to do this, please refer to the README located in https://github.com/pangeo-forge/sandbox.

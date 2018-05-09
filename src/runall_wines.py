## RUN WITH python -m src.runall_wines

import recipy
import importlib

# Import modules
subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

fname = subset.process_data_GBP('data/raw/winemag-data-130k-v2.csv')
print(fname)
plotwines.create_plots(fname)
country_fname = country_sub.get_country(fname, 'Chile')
print(country_fname)
# Dependencies
Requires pdm and python 3.11

https://pdm-project.org/en/latest/#installation

Run `pdm install` to install project dependencies

# Dev

`pdm run dev` \
When running in dev mods, go to /docs to see the swagger \
Dev has hot reload on save


# Run

`pdm run server` \
See `fastapi run --help` to see the available options (such as port and host)

# Routes

`/`: heartbeat, always return "OK" \
`/units`: return a dictionary of units for the nutrional values (e.g.: "mg") \
`/units_number`: return a dictionary of numbers factors of the base unit for the nutrional values (e.g: "mg" becomes 10⁻³) \
`/search/{name}`: returns a dictionary of nutrional values for 100g of the {name} item.


Please refer to the swagger for more precise documentation.

# Adding more fruits or vegetables
Edit `data/fruits_and_vegatables.csv`
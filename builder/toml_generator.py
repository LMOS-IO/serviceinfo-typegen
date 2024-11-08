# TODO: fix deps to match the type defined by config
TOML = '''
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "lmos_serviceinfo_types"
version = "0.1.0"
description = "A Python package for types related to OpenAI"
license = { text = "apache2" }
readme = "README.md"
requires-python = ">=3.7"
dependencies = [
    "pydantic>=2.0"
]

[project.urls]
homepage = "https://github.com/LMOS-IO/serviceinfo-typegen"
repository = "https://github.com/LMOS-IO/serviceinfo-typegen"

[tool.setuptools.packages.find]
where = ["."]
include = ["lmos_serviceinfo_types"]

[tool.setuptools]
package-data = { "lmos_serviceinfo_types" = ["py.typed"] }
'''.strip()

def generate_toml():
    return TOML

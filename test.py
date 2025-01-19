import src.pypixz as pypixz

pypixz.install_modules("pypixz", version_range=">=1.0,!=1.1")

# Install dependencies listed in a requirements.txt file
pypixz.install_requirements("requirements.txt", enable_logging=False)

# Retrieve information from a module.
result = pypixz.get_module_info("pypixz", version="1.1.2")
print(result)

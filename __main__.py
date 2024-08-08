from .model import mainDeconvolver
from . import config

deconvolver = mainDeconvolver.Deconvolver()
deconvolver.setAndLoadData(r'C:\Users\Lattice PC\Documents\Andreas_test\test_stack_with_x_galvo.tif', config.dataPropertiesDict)

# deconvolved = deconvolver.Deconvolve(config.reconOptionsDict, config.algOptionsDict, config.imFormationModelParameters, config.saveOptions)
deconvolver.simpleDeskew(config.algOptionsDict, config.reconOptionsDict, config.saveOptions)

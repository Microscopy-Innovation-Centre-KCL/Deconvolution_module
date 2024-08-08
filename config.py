dataPropertiesDict = {'Camera pixel size [nm]': 101,
                      'Camera offset': 100,
                      'Scan step size [nm]': 105, #105 or 210
                      'Tilt angle [deg]': 30,
                      'Scan axis': 0,
                      'Tilt axis': 1,
                      'Data stacking': 'Linear',
                      'Planes in cycle': 101, # 30 planes for 60 um and 20 planes for 40 um
                      'Cycles': 1, #if 105 nm step size -> 20 cycles, 210 nm -> 10 cycles
                      'Timepoints': 1,
                      'Pos/Neg scan direction': 'Pos'} #Neg in most simulations, Pos in real data

reconOptionsDict = {'Reconstruction voxel size [nm]': 100,
                    'Correct first cycle': False,
                    'Correct pixel offsets': False,
                    'Skew correction pixel per cycle': 0,#~-0.3 used for skewed stage scan
                    'Process timepoints': 'All',
                    'Average timepoints': True}

algOptionsDict = {'Gradient consent': False,
                  'Clip factor for kernel cropping': 0.01,
                  'Iterations': 10}

reconPxSize = str(reconOptionsDict['Reconstruction voxel size [nm]'])
detNA = 1.1#1.1 or 1.26 available now
import os
psfPath = os.path.join(r'PSFs', str(detNA)+'NA', reconPxSize + 'nm', 'PSF_RW_'+str(detNA)+'_' + reconPxSize + 'nmPx_101x101x101.tif')

imFormationModelParameters = {'Optical PSF path': psfPath,
                              'Detection NA': detNA,
                              'Confined sheet FWHM [nm]': 200,
                              'Read-out sheet FWHM [nm]': 1200,
                              'Background sheet ratio': 0.1}

saveOptions = {'Save to disc': True,
               'Save mode': 'Final',
               'Progression mode': 'All',
               'Save folder': r'C:\Users\Lattice PC\Documents\Andreas_test',
               'Save name': 'test_stack_with_x_galvo_recon'}
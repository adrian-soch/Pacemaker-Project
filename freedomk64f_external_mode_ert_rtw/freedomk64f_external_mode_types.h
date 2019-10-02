/*
 * freedomk64f_external_mode_types.h
 *
 * Code generation for model "freedomk64f_external_mode".
 *
 * Model version              : 1.53
 * Simulink Coder version : 9.1 (R2019a) 23-Nov-2018
 * C source code generated on : Tue Oct  1 16:46:58 2019
 *
 * Target selection: ert.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_freedomk64f_external_mode_types_h_
#define RTW_HEADER_freedomk64f_external_mode_types_h_
#include "rtwtypes.h"
#include "multiword_types.h"

/* Custom Type definition for MATLABSystem: '<Root>/FXOS8700 6-Axes Sensor' */
#include "MW_SVD.h"
#ifndef typedef_freedomk64f_Hardware_freedomk_T
#define typedef_freedomk64f_Hardware_freedomk_T

typedef struct {
  int32_T __dummy;
} freedomk64f_Hardware_freedomk_T;

#endif                               /*typedef_freedomk64f_Hardware_freedomk_T*/

#ifndef typedef_freedomk64f_DigitalWrite_free_T
#define typedef_freedomk64f_DigitalWrite_free_T

typedef struct {
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  freedomk64f_Hardware_freedomk_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
} freedomk64f_DigitalWrite_free_T;

#endif                               /*typedef_freedomk64f_DigitalWrite_free_T*/

#ifndef typedef_freedomk64f_I2CMasterWrite_fr_T
#define typedef_freedomk64f_I2CMasterWrite_fr_T

typedef struct {
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  freedomk64f_Hardware_freedomk_T Hw;
  uint32_T BusSpeed;
  MW_Handle_Type MW_I2C_HANDLE;
} freedomk64f_I2CMasterWrite_fr_T;

#endif                               /*typedef_freedomk64f_I2CMasterWrite_fr_T*/

#ifndef typedef_freedomk64f_fxos8700_freedomk_T
#define typedef_freedomk64f_fxos8700_freedomk_T

typedef struct {
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  real_T SampleTime;
  freedomk64f_I2CMasterWrite_fr_T i2cobj;
} freedomk64f_fxos8700_freedomk_T;

#endif                               /*typedef_freedomk64f_fxos8700_freedomk_T*/

/* Parameters (default storage) */
typedef struct P_freedomk64f_external_mode_T_ P_freedomk64f_external_mode_T;

/* Forward declaration for rtModel */
typedef struct tag_RTM_freedomk64f_external__T RT_MODEL_freedomk64f_external_T;

#endif                       /* RTW_HEADER_freedomk64f_external_mode_types_h_ */

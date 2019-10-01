/*
 * freedomk64f_external_mode.h
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

#ifndef RTW_HEADER_freedomk64f_external_mode_h_
#define RTW_HEADER_freedomk64f_external_mode_h_
#include <string.h>
#include <float.h>
#include <stddef.h>
#ifndef freedomk64f_external_mode_COMMON_INCLUDES_
# define freedomk64f_external_mode_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "rtw_extmode.h"
#include "sysran_types.h"
#include "rtw_continuous.h"
#include "rtw_solver.h"
#include "dt_info.h"
#include "ext_work.h"
#include "MW_digitalIO.h"
#include "MW_I2C.h"
#endif                          /* freedomk64f_external_mode_COMMON_INCLUDES_ */

#include "freedomk64f_external_mode_types.h"

/* Shared type includes */
#include "multiword_types.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetFinalTime
# define rtmGetFinalTime(rtm)          ((rtm)->Timing.tFinal)
#endif

#ifndef rtmGetRTWExtModeInfo
# define rtmGetRTWExtModeInfo(rtm)     ((rtm)->extModeInfo)
#endif

#ifndef rtmGetErrorStatus
# define rtmGetErrorStatus(rtm)        ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
# define rtmSetErrorStatus(rtm, val)   ((rtm)->errorStatus = (val))
#endif

#ifndef rtmGetStopRequested
# define rtmGetStopRequested(rtm)      ((rtm)->Timing.stopRequestedFlag)
#endif

#ifndef rtmSetStopRequested
# define rtmSetStopRequested(rtm, val) ((rtm)->Timing.stopRequestedFlag = (val))
#endif

#ifndef rtmGetStopRequestedPtr
# define rtmGetStopRequestedPtr(rtm)   (&((rtm)->Timing.stopRequestedFlag))
#endif

#ifndef rtmGetT
# define rtmGetT(rtm)                  ((rtm)->Timing.taskTime0)
#endif

#ifndef rtmGetTFinal
# define rtmGetTFinal(rtm)             ((rtm)->Timing.tFinal)
#endif

#ifndef rtmGetTPtr
# define rtmGetTPtr(rtm)               (&(rtm)->Timing.taskTime0)
#endif

/* Block signals (default storage) */
typedef struct {
  real_T Gain1[3];                     /* '<Root>/Gain1' */
  real_T y;                            /* '<Root>/MATLAB Function' */
  real_T rtb_FXOS87006AxesSensor_m;
} B_freedomk64f_external_mode_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_fxos8700_freedomk_T obj; /* '<Root>/FXOS8700 6-Axes Sensor' */
  freedomk64f_DigitalWrite_free_T obj_i;/* '<Root>/Digital Write' */
  struct {
    void *LoggedData;
  } Scope1_PWORK;                      /* '<Root>/Scope1' */

  boolean_T objisempty;                /* '<Root>/FXOS8700 6-Axes Sensor' */
  boolean_T objisempty_g;              /* '<Root>/Digital Write' */
} DW_freedomk64f_external_mode_T;

/* Parameters (default storage) */
struct P_freedomk64f_external_mode_T_ {
  real_T Constant_Value;               /* Expression: 0
                                        * Referenced by: '<Root>/Constant'
                                        */
  real_T Constant1_Value;              /* Expression: 1
                                        * Referenced by: '<Root>/Constant1'
                                        */
  real_T FXOS87006AxesSensor_SampleTime;/* Expression: -1
                                         * Referenced by: '<Root>/FXOS8700 6-Axes Sensor'
                                         */
  real_T Gain_Gain;                    /* Expression: 5
                                        * Referenced by: '<Root>/Gain'
                                        */
  real_T Switch_Threshold;             /* Expression: 100
                                        * Referenced by: '<Root>/Switch'
                                        */
  real_T Gain1_Gain;                   /* Expression: 100
                                        * Referenced by: '<Root>/Gain1'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_freedomk64f_external__T {
  const char_T *errorStatus;
  RTWExtModeInfo *extModeInfo;

  /*
   * Sizes:
   * The following substructure contains sizes information
   * for many of the model attributes such as inputs, outputs,
   * dwork, sample times, etc.
   */
  struct {
    uint32_T checksums[4];
  } Sizes;

  /*
   * SpecialInfo:
   * The following substructure contains special information
   * related to other components that are dependent on RTW.
   */
  struct {
    const void *mappingInfo;
  } SpecialInfo;

  /*
   * Timing:
   * The following substructure contains information regarding
   * the timing information for the model.
   */
  struct {
    time_T taskTime0;
    uint32_T clockTick0;
    uint32_T clockTickH0;
    time_T stepSize0;
    time_T tFinal;
    boolean_T stopRequestedFlag;
  } Timing;
};

/* Block parameters (default storage) */
extern P_freedomk64f_external_mode_T freedomk64f_external_mode_P;

/* Block signals (default storage) */
extern B_freedomk64f_external_mode_T freedomk64f_external_mode_B;

/* Block states (default storage) */
extern DW_freedomk64f_external_mode_T freedomk64f_external_mode_DW;

/* Model entry point functions */
extern void freedomk64f_external_mode_initialize(void);
extern void freedomk64f_external_mode_step(void);
extern void freedomk64f_external_mode_terminate(void);

/* Real-time Model object */
extern RT_MODEL_freedomk64f_external_T *const freedomk64f_external_mode_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'freedomk64f_external_mode'
 * '<S1>'   : 'freedomk64f_external_mode/MATLAB Function'
 */
#endif                             /* RTW_HEADER_freedomk64f_external_mode_h_ */

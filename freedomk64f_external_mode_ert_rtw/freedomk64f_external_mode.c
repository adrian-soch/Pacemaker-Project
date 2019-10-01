/*
 * freedomk64f_external_mode.c
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

#include "freedomk64f_external_mode.h"
#include "freedomk64f_external_mode_private.h"
#include "freedomk64f_external_mode_dt.h"

/* Block signals (default storage) */
B_freedomk64f_external_mode_T freedomk64f_external_mode_B;

/* Block states (default storage) */
DW_freedomk64f_external_mode_T freedomk64f_external_mode_DW;

/* Real-time model */
RT_MODEL_freedomk64f_external_T freedomk64f_external_mode_M_;
RT_MODEL_freedomk64f_external_T *const freedomk64f_external_mode_M =
  &freedomk64f_external_mode_M_;

/* Forward declaration for local functions */
static void freedomk64_SystemCore_release_o(const
  freedomk64f_fxos8700_freedomk_T *obj);
static void freedomk64f_SystemCore_delete_o(const
  freedomk64f_fxos8700_freedomk_T *obj);
static void matlabCodegenHandle_matlabCod_o(freedomk64f_fxos8700_freedomk_T *obj);
static void freedomk6_SystemCore_release_oq(freedomk64f_I2CMasterWrite_fr_T *obj);
static void freedomk64_SystemCore_delete_oq(freedomk64f_I2CMasterWrite_fr_T *obj);
static void matlabCodegenHandle_matlabCo_oq(freedomk64f_I2CMasterWrite_fr_T *obj);
static void freedomk64f__SystemCore_release(const
  freedomk64f_DigitalWrite_free_T *obj);
static void freedomk64f_e_SystemCore_delete(const
  freedomk64f_DigitalWrite_free_T *obj);
static void matlabCodegenHandle_matlabCodeg(freedomk64f_DigitalWrite_free_T *obj);
static void freedomk64_SystemCore_release_o(const
  freedomk64f_fxos8700_freedomk_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_I2C_Close(obj->i2cobj.MW_I2C_HANDLE);
  }
}

static void freedomk64f_SystemCore_delete_o(const
  freedomk64f_fxos8700_freedomk_T *obj)
{
  freedomk64_SystemCore_release_o(obj);
}

static void matlabCodegenHandle_matlabCod_o(freedomk64f_fxos8700_freedomk_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    freedomk64f_SystemCore_delete_o(obj);
  }
}

static void freedomk6_SystemCore_release_oq(freedomk64f_I2CMasterWrite_fr_T *obj)
{
  if (obj->isInitialized == 1) {
    obj->isInitialized = 2;
  }
}

static void freedomk64_SystemCore_delete_oq(freedomk64f_I2CMasterWrite_fr_T *obj)
{
  freedomk6_SystemCore_release_oq(obj);
}

static void matlabCodegenHandle_matlabCo_oq(freedomk64f_I2CMasterWrite_fr_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    freedomk64_SystemCore_delete_oq(obj);
  }
}

static void freedomk64f__SystemCore_release(const
  freedomk64f_DigitalWrite_free_T *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_digitalIO_close(obj->MW_DIGITALIO_HANDLE);
  }
}

static void freedomk64f_e_SystemCore_delete(const
  freedomk64f_DigitalWrite_free_T *obj)
{
  freedomk64f__SystemCore_release(obj);
}

static void matlabCodegenHandle_matlabCodeg(freedomk64f_DigitalWrite_free_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    freedomk64f_e_SystemCore_delete(obj);
  }
}

/* Model step function */
void freedomk64f_external_mode_step(void)
{
  int16_T b_output[3];
  uint8_T status;
  uint8_T output_raw[6];
  uint8_T y[2];
  int16_T x;
  uint8_T b_x[2];
  real_T rtb_Gain_idx_0;
  real_T rtb_Gain_idx_1;
  real_T rtb_Gain_idx_2;
  real_T rtb_FXOS87006AxesSensor_idx_0;
  real_T rtb_FXOS87006AxesSensor_idx_1;

  /* MATLABSystem: '<Root>/FXOS8700 6-Axes Sensor' */
  if (freedomk64f_external_mode_DW.obj.SampleTime !=
      freedomk64f_external_mode_P.FXOS87006AxesSensor_SampleTime) {
    freedomk64f_external_mode_DW.obj.SampleTime =
      freedomk64f_external_mode_P.FXOS87006AxesSensor_SampleTime;
  }

  status = 1U;
  status = MW_I2C_MasterWrite
    (freedomk64f_external_mode_DW.obj.i2cobj.MW_I2C_HANDLE, 29U, &status, 1U,
     true, false);
  if (0 == status) {
    MW_I2C_MasterRead(freedomk64f_external_mode_DW.obj.i2cobj.MW_I2C_HANDLE, 29U,
                      output_raw, 6U, false, true);
    memcpy((void *)&b_output[0], (void *)&output_raw[0], (uint32_T)((size_t)3 *
            sizeof(int16_T)));
    x = b_output[0];
    memcpy((void *)&y[0], (void *)&x, (uint32_T)((size_t)2 * sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&b_output[0], (void *)&b_x[0], (uint32_T)((size_t)1 * sizeof
            (int16_T)));
    x = b_output[1];
    memcpy((void *)&y[0], (void *)&x, (uint32_T)((size_t)2 * sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&b_output[1], (void *)&b_x[0], (uint32_T)((size_t)1 * sizeof
            (int16_T)));
    x = b_output[2];
    memcpy((void *)&y[0], (void *)&x, (uint32_T)((size_t)2 * sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&b_output[2], (void *)&b_x[0], (uint32_T)((size_t)1 * sizeof
            (int16_T)));
  } else {
    b_output[0] = 0;
    b_output[1] = 0;
    b_output[2] = 0;
  }

  freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m = (real_T)(int16_T)
    (b_output[0] >> 2) * 2.0 * 0.244 / 1000.0;

  /* Gain: '<Root>/Gain' */
  rtb_Gain_idx_0 = freedomk64f_external_mode_P.Gain_Gain *
    freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m;

  /* MATLABSystem: '<Root>/FXOS8700 6-Axes Sensor' */
  rtb_FXOS87006AxesSensor_idx_0 =
    freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m;
  freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m = (real_T)(int16_T)
    (b_output[1] >> 2) * 2.0 * 0.244 / 1000.0;

  /* Gain: '<Root>/Gain' */
  rtb_Gain_idx_1 = freedomk64f_external_mode_P.Gain_Gain *
    freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m;

  /* MATLABSystem: '<Root>/FXOS8700 6-Axes Sensor' */
  rtb_FXOS87006AxesSensor_idx_1 =
    freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m;
  freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m = (real_T)(int16_T)
    (b_output[2] >> 2) * 2.0 * 0.244 / 1000.0;

  /* Gain: '<Root>/Gain' */
  rtb_Gain_idx_2 = freedomk64f_external_mode_P.Gain_Gain *
    freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m;

  /* MATLAB Function: '<Root>/MATLAB Function' */
  /* MATLAB Function 'MATLAB Function': '<S1>:1' */
  /* '<S1>:1:3' */
  freedomk64f_external_mode_B.y = (rtb_Gain_idx_0 * rtb_Gain_idx_0 +
    rtb_Gain_idx_1 * rtb_Gain_idx_1) + rtb_Gain_idx_2 * rtb_Gain_idx_2;

  /* Switch: '<Root>/Switch' incorporates:
   *  Constant: '<Root>/Constant'
   *  Constant: '<Root>/Constant1'
   */
  if (freedomk64f_external_mode_B.y >
      freedomk64f_external_mode_P.Switch_Threshold) {
    rtb_Gain_idx_0 = freedomk64f_external_mode_P.Constant1_Value;
  } else {
    rtb_Gain_idx_0 = freedomk64f_external_mode_P.Constant_Value;
  }

  /* End of Switch: '<Root>/Switch' */

  /* MATLABSystem: '<Root>/Digital Write' */
  MW_digitalIO_write(freedomk64f_external_mode_DW.obj_i.MW_DIGITALIO_HANDLE,
                     rtb_Gain_idx_0 != 0.0);

  /* Gain: '<Root>/Gain1' */
  freedomk64f_external_mode_B.Gain1[0] = freedomk64f_external_mode_P.Gain1_Gain *
    rtb_FXOS87006AxesSensor_idx_0;
  freedomk64f_external_mode_B.Gain1[1] = freedomk64f_external_mode_P.Gain1_Gain *
    rtb_FXOS87006AxesSensor_idx_1;
  freedomk64f_external_mode_B.Gain1[2] = freedomk64f_external_mode_P.Gain1_Gain *
    freedomk64f_external_mode_B.rtb_FXOS87006AxesSensor_m;

  /* External mode */
  rtExtModeUploadCheckTrigger(1);

  {                                    /* Sample time: [0.001s, 0.0s] */
    rtExtModeUpload(0, (real_T)freedomk64f_external_mode_M->Timing.taskTime0);
  }

  /* signal main to stop simulation */
  {                                    /* Sample time: [0.001s, 0.0s] */
    if ((rtmGetTFinal(freedomk64f_external_mode_M)!=-1) &&
        !((rtmGetTFinal(freedomk64f_external_mode_M)-
           freedomk64f_external_mode_M->Timing.taskTime0) >
          freedomk64f_external_mode_M->Timing.taskTime0 * (DBL_EPSILON))) {
      rtmSetErrorStatus(freedomk64f_external_mode_M, "Simulation finished");
    }

    if (rtmGetStopRequested(freedomk64f_external_mode_M)) {
      rtmSetErrorStatus(freedomk64f_external_mode_M, "Simulation finished");
    }
  }

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++freedomk64f_external_mode_M->Timing.clockTick0)) {
    ++freedomk64f_external_mode_M->Timing.clockTickH0;
  }

  freedomk64f_external_mode_M->Timing.taskTime0 =
    freedomk64f_external_mode_M->Timing.clockTick0 *
    freedomk64f_external_mode_M->Timing.stepSize0 +
    freedomk64f_external_mode_M->Timing.clockTickH0 *
    freedomk64f_external_mode_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void freedomk64f_external_mode_initialize(void)
{
  /* Registration code */

  /* initialize real-time model */
  (void) memset((void *)freedomk64f_external_mode_M, 0,
                sizeof(RT_MODEL_freedomk64f_external_T));
  rtmSetTFinal(freedomk64f_external_mode_M, -1);
  freedomk64f_external_mode_M->Timing.stepSize0 = 0.001;

  /* External mode info */
  freedomk64f_external_mode_M->Sizes.checksums[0] = (3643065822U);
  freedomk64f_external_mode_M->Sizes.checksums[1] = (474249077U);
  freedomk64f_external_mode_M->Sizes.checksums[2] = (1608407433U);
  freedomk64f_external_mode_M->Sizes.checksums[3] = (165817490U);

  {
    static const sysRanDType rtAlwaysEnabled = SUBSYS_RAN_BC_ENABLE;
    static RTWExtModeInfo rt_ExtModeInfo;
    static const sysRanDType *systemRan[6];
    freedomk64f_external_mode_M->extModeInfo = (&rt_ExtModeInfo);
    rteiSetSubSystemActiveVectorAddresses(&rt_ExtModeInfo, systemRan);
    systemRan[0] = &rtAlwaysEnabled;
    systemRan[1] = &rtAlwaysEnabled;
    systemRan[2] = &rtAlwaysEnabled;
    systemRan[3] = &rtAlwaysEnabled;
    systemRan[4] = &rtAlwaysEnabled;
    systemRan[5] = &rtAlwaysEnabled;
    rteiSetModelMappingInfoPtr(freedomk64f_external_mode_M->extModeInfo,
      &freedomk64f_external_mode_M->SpecialInfo.mappingInfo);
    rteiSetChecksumsPtr(freedomk64f_external_mode_M->extModeInfo,
                        freedomk64f_external_mode_M->Sizes.checksums);
    rteiSetTPtr(freedomk64f_external_mode_M->extModeInfo, rtmGetTPtr
                (freedomk64f_external_mode_M));
  }

  /* block I/O */
  (void) memset(((void *) &freedomk64f_external_mode_B), 0,
                sizeof(B_freedomk64f_external_mode_T));

  /* states (dwork) */
  (void) memset((void *)&freedomk64f_external_mode_DW, 0,
                sizeof(DW_freedomk64f_external_mode_T));

  /* data type transition information */
  {
    static DataTypeTransInfo dtInfo;
    (void) memset((char_T *) &dtInfo, 0,
                  sizeof(dtInfo));
    freedomk64f_external_mode_M->SpecialInfo.mappingInfo = (&dtInfo);
    dtInfo.numDataTypes = 16;
    dtInfo.dataTypeSizes = &rtDataTypeSizes[0];
    dtInfo.dataTypeNames = &rtDataTypeNames[0];

    /* Block I/O transition table */
    dtInfo.BTransTable = &rtBTransTable;

    /* Parameters transition table */
    dtInfo.PTransTable = &rtPTransTable;
  }

  {
    freedomk64f_fxos8700_freedomk_T *obj;
    uint32_T i2cname;
    uint8_T b_SwappedDataBytes[2];
    uint8_T b_RegisterValue;
    uint8_T status;
    freedomk64f_DigitalWrite_free_T *obj_0;

    /* Start for MATLABSystem: '<Root>/FXOS8700 6-Axes Sensor' */
    freedomk64f_external_mode_DW.obj.i2cobj.matlabCodegenIsDeleted = true;
    freedomk64f_external_mode_DW.obj.matlabCodegenIsDeleted = true;
    obj = &freedomk64f_external_mode_DW.obj;
    freedomk64f_external_mode_DW.obj.isInitialized = 0;
    freedomk64f_external_mode_DW.obj.SampleTime = -1.0;
    obj->i2cobj.isInitialized = 0;
    obj->i2cobj.matlabCodegenIsDeleted = false;

    /* [EOF] */
    /*  */
    freedomk64f_external_mode_DW.obj.matlabCodegenIsDeleted = false;
    freedomk64f_external_mode_DW.objisempty = true;
    freedomk64f_external_mode_DW.obj.SampleTime =
      freedomk64f_external_mode_P.FXOS87006AxesSensor_SampleTime;
    obj = &freedomk64f_external_mode_DW.obj;
    freedomk64f_external_mode_DW.obj.isSetupComplete = false;
    freedomk64f_external_mode_DW.obj.isInitialized = 1;
    i2cname = 0;
    obj->i2cobj.MW_I2C_HANDLE = MW_I2C_Open(i2cname, 0);

    /* KHz */
    obj->i2cobj.BusSpeed = 100000U;
    MW_I2C_SetBusSpeed(obj->i2cobj.MW_I2C_HANDLE, obj->i2cobj.BusSpeed);
    b_SwappedDataBytes[0] = 43U;
    b_SwappedDataBytes[1] = 64U;
    MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, b_SwappedDataBytes, 2U,
                       false, false);
    OSA_TimeDelay(500U);
    status = 42U;
    status = MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, &status, 1U,
      true, false);
    if (0 == status) {
      MW_I2C_MasterRead(obj->i2cobj.MW_I2C_HANDLE, 29U, &status, 1U, false, true);
      memcpy((void *)&b_RegisterValue, (void *)&status, (uint32_T)((size_t)1 *
              sizeof(uint8_T)));
    } else {
      b_RegisterValue = 0U;
    }

    b_SwappedDataBytes[0] = 42U;
    b_SwappedDataBytes[1] = (uint8_T)(b_RegisterValue & 254);
    MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, b_SwappedDataBytes, 2U,
                       false, false);
    b_SwappedDataBytes[0] = 14U;
    b_SwappedDataBytes[1] = 1U;
    MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, b_SwappedDataBytes, 2U,
                       false, false);
    b_SwappedDataBytes[0] = 91U;
    b_SwappedDataBytes[1] = 0U;
    MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, b_SwappedDataBytes, 2U,
                       false, false);
    b_SwappedDataBytes[0] = 42U;
    b_SwappedDataBytes[1] = 9U;
    MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, b_SwappedDataBytes, 2U,
                       false, false);
    freedomk64f_external_mode_DW.obj.isSetupComplete = true;

    /* End of Start for MATLABSystem: '<Root>/FXOS8700 6-Axes Sensor' */

    /* Start for MATLABSystem: '<Root>/Digital Write' */
    freedomk64f_external_mode_DW.obj_i.matlabCodegenIsDeleted = true;
    freedomk64f_external_mode_DW.obj_i.isInitialized = 0;
    freedomk64f_external_mode_DW.obj_i.matlabCodegenIsDeleted = false;
    freedomk64f_external_mode_DW.objisempty_g = true;

    /* [EOF] */
    obj_0 = &freedomk64f_external_mode_DW.obj_i;
    freedomk64f_external_mode_DW.obj_i.isSetupComplete = false;
    freedomk64f_external_mode_DW.obj_i.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(43U, 1);
    freedomk64f_external_mode_DW.obj_i.isSetupComplete = true;
  }
}

/* Model terminate function */
void freedomk64f_external_mode_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/FXOS8700 6-Axes Sensor' */
  matlabCodegenHandle_matlabCod_o(&freedomk64f_external_mode_DW.obj);
  matlabCodegenHandle_matlabCo_oq(&freedomk64f_external_mode_DW.obj.i2cobj);

  /* Terminate for MATLABSystem: '<Root>/Digital Write' */
  matlabCodegenHandle_matlabCodeg(&freedomk64f_external_mode_DW.obj_i);
}

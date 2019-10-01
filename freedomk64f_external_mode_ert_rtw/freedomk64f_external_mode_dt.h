/*
 * freedomk64f_external_mode_dt.h
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

#include "ext_types.h"

/* data type size table */
static uint_T rtDataTypeSizes[] = {
  sizeof(real_T),
  sizeof(real32_T),
  sizeof(int8_T),
  sizeof(uint8_T),
  sizeof(int16_T),
  sizeof(uint16_T),
  sizeof(int32_T),
  sizeof(uint32_T),
  sizeof(boolean_T),
  sizeof(fcn_call_T),
  sizeof(int_T),
  sizeof(pointer_T),
  sizeof(action_T),
  2*sizeof(uint32_T),
  sizeof(freedomk64f_DigitalWrite_free_T),
  sizeof(freedomk64f_fxos8700_freedomk_T)
};

/* data type name table */
static const char_T * rtDataTypeNames[] = {
  "real_T",
  "real32_T",
  "int8_T",
  "uint8_T",
  "int16_T",
  "uint16_T",
  "int32_T",
  "uint32_T",
  "boolean_T",
  "fcn_call_T",
  "int_T",
  "pointer_T",
  "action_T",
  "timer_uint32_pair_T",
  "freedomk64f_DigitalWrite_free_T",
  "freedomk64f_fxos8700_freedomk_T"
};

/* data type transitions for block I/O structure */
static DataTypeTransition rtBTransitions[] = {
  { (char_T *)(&freedomk64f_external_mode_B.Gain1[0]), 0, 0, 4 }
  ,

  { (char_T *)(&freedomk64f_external_mode_DW.obj), 15, 0, 1 },

  { (char_T *)(&freedomk64f_external_mode_DW.obj_i), 14, 0, 1 },

  { (char_T *)(&freedomk64f_external_mode_DW.Scope1_PWORK.LoggedData), 11, 0, 1
  },

  { (char_T *)(&freedomk64f_external_mode_DW.objisempty), 8, 0, 2 }
};

/* data type transition table for block I/O structure */
static DataTypeTransitionTable rtBTransTable = {
  5U,
  rtBTransitions
};

/* data type transitions for Parameters structure */
static DataTypeTransition rtPTransitions[] = {
  { (char_T *)(&freedomk64f_external_mode_P.Constant_Value), 0, 0, 6 }
};

/* data type transition table for Parameters structure */
static DataTypeTransitionTable rtPTransTable = {
  1U,
  rtPTransitions
};

/* [EOF] freedomk64f_external_mode_dt.h */

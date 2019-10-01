/*
 * freedomk64f_external_mode_tgtconn.c
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

#include "rtwtypes.h"
#define EXTERN_C
#include <stdio.h>
#include "RTIOStreamTgtAppSvc/RTIOStreamTgtAppSvcCIntrf.h"

extern void initializeCommService( );
extern void terminateCommService();
EXTERN_C void TgtConnBackgroundTask()
{
}

EXTERN_C const char *TgtConnInit(int_T argc, char_T *argv[])
{
  const char *result = NULL;           /* assume success */
  initializeCommService( );
  return(result);
}

EXTERN_C void TgtConnTerm()
{
  terminateCommService();
}

EXTERN_C void TgtConnPreStep(int_T tid)
{
}

EXTERN_C void TgtConnPostStep(int_T tid)
{
}

/* EOF: freedomk64f_external_mode_tgtconn.c */

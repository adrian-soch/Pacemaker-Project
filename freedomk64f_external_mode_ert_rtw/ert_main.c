#include "freedomk64f_external_mode.h"
#include "freedomk64f_external_mode_private.h"
#include "rtwtypes.h"
#include "limits.h"
#include "board.h"
#include "mw_cmsis_rtos.h"
#define UNUSED(x)                      x = x
#define NAMELEN                        16
#define EXIT_ON_ERROR(msg, cond)       if (cond) { return(0); }

extern const char *TgtConnInit(int_T argc, char_T *argv[]);
extern void TgtConnTerm();
extern void TgtConnPreStep(int_T tid);
extern void TgtConnPostStep(int_T tid);
const char * csErrorStatus;

/* Function prototype declaration*/
void exitFcn(int sig);
void *terminateTask(void *arg);
void *baseRateTask(void *arg);
void *subrateTask(void *arg);
volatile boolean_T stopRequested = false;
volatile boolean_T runModel = true;
mw_signal_event_t stopSem;
mw_signal_event_t baserateTaskSem;
mw_thread_t schedulerThread;
mw_thread_t baseRateThread;
mw_thread_t backgroundThread;
void *threadJoinStatus;
int terminatingmodel = 0;
void *baseRateTask(void *arg)
{
  runModel = (rtmGetErrorStatus(freedomk64f_external_mode_M) == (NULL)) &&
    !rtmGetStopRequested(freedomk64f_external_mode_M);
  while (runModel) {
    mw_osSignalEventWaitEver(&baserateTaskSem);

    /* External mode */
    {
      boolean_T rtmStopReq = false;
      rtExtModePauseIfNeeded(freedomk64f_external_mode_M->extModeInfo, 1,
        &rtmStopReq);
      if (rtmStopReq) {
        rtmSetStopRequested(freedomk64f_external_mode_M, true);
      }

      if (rtmGetStopRequested(freedomk64f_external_mode_M) == true) {
        rtmSetErrorStatus(freedomk64f_external_mode_M, "Simulation finished");
        break;
      }
    }

    freedomk64f_external_mode_step();

    /* Get model outputs here */
    rtExtModeCheckEndTrigger();
    stopRequested = !((rtmGetErrorStatus(freedomk64f_external_mode_M) == (NULL))
                      && !rtmGetStopRequested(freedomk64f_external_mode_M));
    runModel = !stopRequested;
  }

  runModel = 0;
  terminateTask(arg);
  mw_osThreadExit((void *)0);
  return NULL;
}

void exitFcn(int sig)
{
  UNUSED(sig);
  rtmSetErrorStatus(freedomk64f_external_mode_M, "stopping the model");
  runModel = 0;
}

void *terminateTask(void *arg)
{
  UNUSED(arg);
  terminatingmodel = 1;

  {
    runModel = 0;

    /* Wait for background task to complete */
    CHECK_STATUS(mw_osThreadJoin(backgroundThread, &threadJoinStatus), 0,
                 "mw_osThreadJoin");
  }

  /* Disable rt_OneStep() here */

  /* Terminate model */
  freedomk64f_external_mode_terminate();
  rtExtModeShutdown(1);
  TgtConnTerm();
  mw_osSignalEventRelease(&stopSem);
  return NULL;
}

void *backgroundTask(void *arg)
{
  while (runModel) {
    /* External mode */
    {
      boolean_T rtmStopReq = false;
      rtExtModeOneStep(freedomk64f_external_mode_M->extModeInfo, 1, &rtmStopReq);
      if (rtmStopReq) {
        rtmSetStopRequested(freedomk64f_external_mode_M, true);
      }
    }

    runCommService();
  }

  return NULL;
}

int main(int argc, char **argv)
{
  SystemCoreClockUpdate();
  hardware_init();
  rtmSetErrorStatus(freedomk64f_external_mode_M, 0);
  rtExtModeParseArgs(argc, (const char_T **)argv, NULL);

  /* Target connectivity initialization */
  csErrorStatus = TgtConnInit(argc, argv);
  EXIT_ON_ERROR("Error initializing target connectivity: %s\n", csErrorStatus);

  /* Initialize model */
  freedomk64f_external_mode_initialize();

  /* External mode */
  rtSetTFinalForExtMode(&rtmGetTFinal(freedomk64f_external_mode_M));
  rtExtModeCheckInit(1);

  {
    boolean_T rtmStopReq = false;
    rtExtModeWaitForStartPkt(freedomk64f_external_mode_M->extModeInfo, 1,
      &rtmStopReq);
    if (rtmStopReq) {
      rtmSetStopRequested(freedomk64f_external_mode_M, true);
    }
  }

  rtERTExtModeStartMsg();

  /* Call RTOS Initialization function */
  mw_RTOSInit(0.001, 0);

  /* Wait for stop semaphore */
  mw_osSignalEventWaitEver(&stopSem);

#if (MW_NUMBER_TIMER_DRIVEN_TASKS > 0)

  {
    int i;
    for (i=0; i < MW_NUMBER_TIMER_DRIVEN_TASKS; i++) {
      CHECK_STATUS(mw_osSignalEventDelete(&timerTaskSem[i]), 0,
                   "mw_osSignalEventDelete");
    }
  }

#endif

  return 0;
}

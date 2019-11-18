import serial
import numpy
from DCMv2 import *

def aoo_data_output(aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry):

    state = "aoo"
    lowerRateLimit = aoo_lowerRateLimitEntry
    upperRateLimit = aoo_upperRateLimitEntry
    atrialAmplitude = aoo_atrialAmplitudeEntry
    atrialPulseWidth = aoo_atrialPulseWidthEntry

    data_output = [state, lowerRateLimit, upperRateLimit, atrialAmplitude, atrialPulseWidth]
    serial_data_output = str.encode(data_output)

def voo_data_output(voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry):

    state = "voo"
    lowerRateLimit = voo_lowerRateLimitEntry
    upperRateLimit = voo_upperRateLimitEntry
    ventricularAmplitude = voo_ventricularAmplitudeEntry
    ventricularPulseWidth = voo_ventricularPulseWidthEntry

    data_output = [state, lowerRateLimit, upperRateLimit, ventricularAmplitude, ventricularPulseWidth]
    serial_data_output = str.encode(data_output)

def aii_data_ouput(aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,):

    state = "aii"
    lowerRateLimit = aai_lowerRateLimitEntry
    upperRateLimit = aai_upperRateLimitEntry
    atrialAmplitude = aai_atrialAmplitudeEntry
    atrialPulseWidth = aai_atrialPulseWidthEntry
    atrialSensitivity = aai_atrialSensitivityEntry
    ARP = aai_ARPEntry
    PVRAP = aai_PVARPEntry

    data_output = [state, lowerRateLimit, upperRateLimit, atrialAmplitude, atrialPulseWidth, atrialSensitivity, ARP, PVRAP]
    serial_data_output = str.encode(data_output)

def vvi_data_output(vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry):

    state = "vvi"
    lowerRateLimit = vvi_lowerRateLimitEntry
    upperRateLimit = vvi_upperRateLimitEntry
    ventricularAmplitude = vvi_ventricularAmplitudeEntry
    ventricularPulseWidth = vvi_ventricularPulseWidthEntry
    ventricularSensitivity = vvi_ventricularSensitivityEntry
    VRP = vvi_VRPEntry

    data_output = [state, lowerRateLimit, upperRateLimit, ventricularAmplitude, ventricularPulseWidth, ventricularSensitivity, VRP]
    serial_data_output = str.encode(data_output)

def doo_data_output(doo_lowerRateLimitEntry, doo_upperRateLimitEntry, doo_atrialAmplitudeEntry, doo_atrialPulseWidthEntry, doo_ventricularAmplitudeEntry, doo_ventricularPulseWidthEntry, doo_fixedAVDelayEntry):
    
    state = "doo"
    lowerRateLimit = doo_lowerRateLimitEntry
    upperRateLimit = doo_upperRateLimitEntry
    atrialAmplitude = doo_atrialAmplitudeEntry
    ventricularAmplitude = doo_ventricularAmplitudeEntry
    atrialPulseWidth = doo_atrialPulseWidthEntry
    fixedAVDelay = doo_fixedAVDelayEntry

    data_output = [state, lowerRateLimit, upperRateLimit, atrialAmplitude, ventricularAmplitude, atrialAmplitude, fixedAVDelay]
    serial_data_output = str.encode(data_output)

def aoor_data_output(aoor_lowerRateLimitEntry, aoor_upperRateLimitEntry, aoor_atrialAmplitudeEntry, aoor_atrialPulseWidthEntry, aoor_maximumSensorRateEntry, aoor_activityThresholdEntry, aoor_reactionTimeEntry, aoor_responseFactorEntry, aoor_recoveryTimeEntry):
    
    state = "aoor"
    lowerRateLimit = aoor_lowerRateLimitEntry
    upperRateLimit = aoor_upperRateLimitEntry
    atrialAmplitude = aoor_atrialAmplitudeEntry
    atrialPulseWidth = aoor_atrialPulseWidthEntry
    atrialMaximumSensorRate = aoor_maximumSensorRateEntry
    activityThreshold = aoor_activityThresholdEntry
    reactionTime = aoor_reactionTimeEntry
    responseFactor  = aoor_responseFactorEntry
    recoveryTime = aoor_recoveryTimeEntry

    data_output = [state, lowerRateLimit, upperRateLimit, atrialAmplitude, atrialPulseWidth, atrialMaximumSensorRate, activityThreshold, reactionTime, responseFactor, recoveryTime]
    serial_data_output = str.encode(data_output)
    
    return serial_data_output
    
def voor_data_output(voor_lowerRateLimitEntry, voor_upperRateLimitEntry, voor_ventricularAmplitudeEntry, voor_ventricularPulseWidthEntry, voor_maximumSensorRateEntry, voor_activityThresholdEntry, voor_reactionTimeEntry, voor_responseFactorEntry, voor_recoveryTimeEntry):

    state = "voor"
    lowerRateLimit = voor_lowerRateLimitEntry
    upperRateLimit = voor_upperRateLimitEntry
    ventricularAmplitude = voor_ventricularAmplitudeEntry
    ventricularPulseWidth = voor_ventricularPulseWidthEntry
    maximumSensorRate = voor_maximumSensorRateEntry
    activityThresholdEntry = voor_activityThresholdEntry
    reactionTime = voor_reactionTimeEntry
    responseFactor = voor_responseFactorEntry
    recoveryTime = voor_recoveryTimeEntry
    
    data_output = [state, lowerRateLimit, upperRateLimit, ventricularAmplitude, ventricularPulseWidth, maximumSensorRate, activityThresholdEntry, reactionTime, responseFactor, recoveryTime]
    serial_data_output = str.encode(data_output)
    
    return serial_data_output
    
def aair_data_output(aair_lowerRateLimitEntry, aair_upperRateLimitEntry, aair_atrialAmplitudeEntry, aair_atrialPulseWidthEntry, aair_atrialSensitivityEntry, aair_ARPEntry, aair_PVARPEntry, aair_hysteresisEntry, aair_rateSmoothingEntry, aair_maximumSensorRateEntry, aair_activityThresholdEntry, aair_reactionTimeEntry, aair_responseFactorEntry, aair_recoveryTimeEntry):

    state = "aair"
    lowerRateLimit = aair_lowerRateLimitEntry
    upperRateLimit = aair_upperRateLimitEntry
    atrialAmplitude = aair_atrialAmplitudeEntry
    atrialPulseWidth = aair_atrialPulseWidthEntry
    atrialSensitivity = aair_atrialSensitivityEntry
    ARP = aair_ARPEntry
    PVARP = aair_PVARPEntry
    maximumSensorRate = aair_maximumSensorRateEntry
    activityThreshold = aair_activityThresholdEntry
    reactionTime = aair_reactionTimeEntry
    responseFactor = aair_responseFactorEntry
    recoveryTime = aair_recoveryTimeEntry

    data_output = [state, lowerRateLimit, upperRateLimit, atrialAmplitude, atrialPulseWidth, atrialSensitivity, ARP, PVARP, maximumSensorRate, activityThreshold, reactionTime, responseFactor, recoveryTime]
    serial_data_output = str.encode(data_output)
    return serial_data_output
    

def vvir_data_output(vvir_lowerRateLimitEntry, vvir_upperRateLimitEntry, vvir_ventricularAmplitudeEntry, vvir_ventricularPulseWidthEntry, vvir_ventricularSensitivityEntry, vvir_VRPEntry, vvir_hysteresisEntry, vvir_rateSmoothingEntry, vvir_maximumSensorRateEntry, vvir_activityThresholdEntry, vvir_reactionTimeEntry, vvir_responseFactorEntry, vvir_recoveryTimeEntry):
    
    state = "vvir"
    lowerRateLimit = vvir_lowerRateLimitEntry
    upperRateLimit = vvir_upperRateLimitEntry
    ventricularAmplitude = vvir_ventricularAmplitudeEntry
    ventricularPulseWidth = vvir_ventricularPulseWidthEntry
    ventricularSensitivity = vvir_ventricularSensitivityEntry
    VRP = vvir_VRPEntry
    maximumSensorRate = vvir_maximumSensorRateEntry
    activityThreshold = vvir_activityThresholdEntry
    reactionTimeEntry = vvir_reactionTimeEntry
    responseFactorEntry = vvir_responseFactorEntry
    recoveryTimeEntry = vvir_recoveryTimeEntry

    data_output = [state, lowerRateLimit, upperRateLimit, ventricularAmplitude, ventricularPulseWidth, ventricularSensitivity, VRP, maximumSensorRate, fixedAVDelay, activityThreshold, reactionTime, responseFactor, recoveryTime]
    serial_data_output = str.encode(data_output)
    return serial_data_output
    

def door_data_output(door_lowerRateLimitEntry, door_upperRateLimitEntry, door_atrialAmplitudeEntry, door_atrialPulseWidthEntry, door_ventricularAmplitudeEntry, door_ventricularPulseWidthEntry, door_maximumSensorRateEntry, door_fixedAVDelayEntry, door_activityThresholdEntry, door_reactionTimeEntry, door_responseFactorEntry, door_recoveryTimeEntry):
    
    state = "door"
    lowerRateLimit = door_lowerRateLimitEntry
    upperRateLimit = door_upperRateLimitEntry
    atrialAmplitude = door_atrialAmplitudeEntry
    atrialPulseWidth = door_atrialPulseWidthEntry
    ventricularAmplitude = door_ventricularAmplitudeEntry
    ventricularPulseWidth = door_ventricularPulseWidthEntry
    maximumSensorRate = door_maximumSensorRateEntry
    fixedAVDelay = door_fixedAVDelayEntry
    activityThreshold = door_activityThresholdEntry
    reactionTime = door_reactionTimeEntry
    responseFactor = door_responseFactorEntry
    recoveryTime = door_recoveryTimeEntry

    data_output = [state, lowerRateLimit, upperRateLimit, atrialAmplitude, atrialPulseWidth, ventricularAmplitude, ventricularPulseWidth, maximumSensorRate, fixedAVDelay, activityThreshold, reactionTime, responseFactor, recoveryTime]
    serial_data_output = str.encode(data_output)
    return serial_data_output

def main():

    global state
    global aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry
    global voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry
    global aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry
    global vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry
    global doo_lowerRateLimitEntry, doo_upperRateLimitEntry, doo_atrialAmplitudeEntry, doo_atrialPulseWidthEntry, doo_ventricularAmplitudeEntry, doo_ventricularPulseWidthEntry, doo_fixedAVDelayEntry
    global aoor_lowerRateLimitEntry, aoor_upperRateLimitEntry, aoor_atrialAmplitudeEntry, aoor_atrialPulseWidthEntry, aoor_maximumSensorRateEntry, aoor_activityThresholdEntry, aoor_reactionTimeEntry, aoor_responseFactorEntry, aoor_recoveryTimeEntry
    global voor_lowerRateLimitEntry, voor_upperRateLimitEntry, voor_ventricularAmplitudeEntry, voor_ventricularPulseWidthEntry, voor_maximumSensorRateEntry, voor_activityThresholdEntry, voor_reactionTimeEntry, voor_responseFactorEntry, voor_recoveryTimeEntry
    global aair_lowerRateLimitEntry, aair_upperRateLimitEntry, aair_atrialAmplitudeEntry, aair_atrialPulseWidthEntry, aair_atrialSensitivityEntry, aair_ARPEntry, aair_PVARPEntry, aair_hysteresisEntry, aair_rateSmoothingEntry, aair_maximumSensorRateEntry, aair_activityThresholdEntry, aair_reactionTimeEntry, aair_responseFactorEntry, aair_recoveryTimeEntry
    global vvir_lowerRateLimitEntry, vvir_upperRateLimitEntry, vvir_ventricularAmplitudeEntry, vvir_ventricularPulseWidthEntry, vvir_ventricularSensitivityEntry, vvir_VRPEntry, vvir_hysteresisEntry, vvir_rateSmoothingEntry, vvir_maximumSensorRateEntry, vvir_activityThresholdEntry, vvir_reactionTimeEntry, vvir_responseFactorEntry, vvir_recoveryTimeEntry
    global door_lowerRateLimitEntry, door_upperRateLimitEntry, door_atrialAmplitudeEntry, door_atrialPulseWidthEntry, door_ventricularAmplitudeEntry, door_ventricularPulseWidthEntry, door_maximumSensorRateEntry, door_fixedAVDelayEntry, door_activityThresholdEntry, door_reactionTimeEntry, door_responseFactorEntry, door_recoveryTimeEntry


    if (state == "aooConfirm"):
        data_out = aoo_data_output(aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry)
    
    elif (state == "vooConfirm"):
        data_out = voo_data_output(voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry)
    
    elif (state == "aaiConfirm"):
        data_out = aai_data_output(aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry)
    
    elif (state == "vviConfirm"):
        data_out = vvi_data_output(vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry,0,vvi_hysteresisEntry,vvi_rateSmoothingEntry)

    elif (state == "dooConfirm"):
        data_out = doo_data_output(doo_lowerRateLimitEntry, doo_upperRateLimitEntry, doo_atrialAmplitudeEntry, doo_atrialPulseWidthEntry, doo_ventricularAmplitudeEntry, doo_ventricularPulseWidthEntry, doo_fixedAVDelayEntry)

    elif (state == "aoorConfirm"):
        data_out = aoor_data_output(aoor_lowerRateLimitEntry, aoor_upperRateLimitEntry, aoor_atrialAmplitudeEntry, aoor_atrialPulseWidthEntry, aoor_maximumSensorRateEntry, aoor_activityThresholdEntry, aoor_reactionTimeEntry, aoor_responseFactorEntry, aoor_recoveryTimeEntry)

    elif (state == "voorConfirm"):
        data_out = voor_data_output(voor_lowerRateLimitEntry, voor_upperRateLimitEntry, voor_ventricularAmplitudeEntry, voor_ventricularPulseWidthEntry, voor_maximumSensorRateEntry, voor_activityThresholdEntry, voor_reactionTimeEntry, voor_responseFactorEntry, voor_recoveryTimeEntry)
    
    elif (state == "aairConfirm"):
        data_out = aair_data_output(aair_lowerRateLimitEntry, aair_upperRateLimitEntry, aair_atrialAmplitudeEntry, aair_atrialPulseWidthEntry, aair_atrialSensitivityEntry, aair_ARPEntry, aair_PVARPEntry, aair_hysteresisEntry, aair_rateSmoothingEntry, aair_maximumSensorRateEntry, aair_activityThresholdEntry, aair_reactionTimeEntry, aair_responseFactorEntry, aair_recoveryTimeEntry)

    elif (state == "vvirConfirm"):
        data_out = vvir_data_output(vvir_lowerRateLimitEntry, vvir_upperRateLimitEntry, vvir_ventricularAmplitudeEntry, vvir_ventricularPulseWidthEntry, vvir_ventricularSensitivityEntry, vvir_VRPEntry, vvir_hysteresisEntry, vvir_rateSmoothingEntry, vvir_maximumSensorRateEntry, vvir_activityThresholdEntry, vvir_reactionTimeEntry, vvir_responseFactorEntry, vvir_recoveryTimeEntry)

    elif (state == "doorConfirm"): 
        data_out = door_data_output(door_lowerRateLimitEntry, door_upperRateLimitEntry, door_atrialAmplitudeEntry, door_atrialPulseWidthEntry, door_ventricularAmplitudeEntry, door_ventricularPulseWidthEntry, door_maximumSensorRateEntry, door_fixedAVDelayEntry, door_activityThresholdEntry, door_reactionTimeEntry, door_responseFactorEntry, door_recoveryTimeEntry)

    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'COM3'
    ser.open()

    ser.write(data_out)

    ser.close() 

    

if __name__ == '__main__':
    main()



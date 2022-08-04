
#ifndef OVRMETRICSTOOL_H
#define OVRMETRICSTOOL_H

#ifdef __cplusplus
extern "C" {
#endif

#include <jni.h>

// ovrMetricsTool_Initialize must be called before making other calls.
bool ovrMetricsTool_Initialize(JavaVM* jvm, JNIEnv* jni, jobject context);
bool ovrMetricsTool_InitializeWithClassLoader(
    JavaVM* jvm,
    JNIEnv* jni,
    jobject context,
    jobject classLoader);

// You should call this when vrapi_EnterVrMode is called.
bool ovrMetricsTool_EnterVrMode();

bool ovrMetricsTool_AppendCsvDebugString(const char* format, ...)
    __attribute__((format(printf, 1, 2)));

bool ovrMetricsTool_SetOverlayDebugString(const char* format, ...)
    __attribute__((format(printf, 1, 2)));

// return value will be allocated on the heap!
char* ovrMetricsTool_GetLatestEventJson();

// You should call ovrMetricsTool_LeaveVrMode when vrapi_LeaveVrMode is called.
void ovrMetricsTool_LeaveVrMode();

// ovrMetricsTool_Shutdown must be the last function called
void ovrMetricsTool_Shutdown();

#ifdef __cplusplus
}
#endif

#endif

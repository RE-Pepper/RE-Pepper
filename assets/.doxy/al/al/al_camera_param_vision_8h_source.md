

# File alCameraParamVision.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Camera**](dir_379bdf7de792c5b2fa4c12f230f357ac.md) **>** [**alCameraParamVision.h**](al_camera_param_vision_8h.md)

[Go to the documentation of this file](al_camera_param_vision_8h.md)


```C++
#pragma once

namespace al
{

class ByamlIter;

class CameraParamVision
{
private:
        float mFovyDegree;
        float mStereovisionDistance;
        float mStereovisionDepth;
        float mNearClipDistance;
        float mFarClipDistance;

public:
        bool init( const ByamlIter* ticket );

public:
        CameraParamVision();
};

} // namespace al
```



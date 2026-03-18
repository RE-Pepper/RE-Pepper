

# File alCamera.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Camera**](dir_b39408af9c4561f6cdf388b41f39f7f7.md) **>** [**alCamera.h**](al_camera_8h.md)

[Go to the documentation of this file](al_camera_8h.md)


```C++
#pragma once

#include <math/seadVector.h>

namespace al
{
class ByamlIter;
class CameraParamVision;
class CameraDashAngleTunerParam;
class CameraRotatorParam;

class CameraUnknownParam
{
        u8 _0;

public:
        CameraUnknownParam() : _0( 0 )
        {
        }
};

class Camera
{
private:
        const char* const mName;

protected:
        sead::Vector3f             _8;
        sead::Vector3f             mPos;
        sead::Vector3f             mTarget;
        sead::Vector3f             _2C;
        int                        mInterpoleFrame;
        CameraParamVision*         mVisionParam;
        CameraDashAngleTunerParam* mDashAngleTunerParam;
        CameraUnknownParam*        mUnknownParam;
        CameraRotatorParam*        mRotatorParam;

public:
        virtual void load( const ByamlIter* ticket );
        virtual void v1();
        virtual void v2();
        virtual void v3();
        virtual void v4();
        virtual void v5();
        virtual void calc();
        virtual void v7();

public:
        Camera( const char* name );
};

const sead::Vector3f* getCameraPos();

} // namespace al
```



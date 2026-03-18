

# File alCameraParamVision.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Camera**](dir_ae22786bedc4ead2a439ef673b994a37.md) **>** [**alCameraParamVision.cpp**](al_camera_param_vision_8cpp.md)

[Go to the documentation of this file](al_camera_param_vision_8cpp.md)


```C++
#include <Camera/alCameraParamVision.h>
#include <Yaml/alByamlIter.h>

namespace al
{

CameraParamVision::CameraParamVision()
{
        mNearClipDistance     = -1.0;
        mFarClipDistance      = -1.0;
        mFovyDegree           = 45.0;
        mStereovisionDistance = 200.0;
        mStereovisionDepth    = 1.0;
}

bool CameraParamVision::init( const ByamlIter* ticket )
{
        ByamlIter h;
        if ( ticket->tryGetIterByKey( &h, "VisionParam" ) )
        {
                h.tryGetFloatByKey( &mFovyDegree, "FovyDegree" );
                h.tryGetFloatByKey( &mStereovisionDistance, "StereovisionDistance" );
                h.tryGetFloatByKey( &mStereovisionDepth, "StereovisionDepth" );
                h.tryGetFloatByKey( &mNearClipDistance, "NearClipDistacne" );
                h.tryGetFloatByKey( &mFarClipDistance, "FarClipDistance" );
                return true;
        }
        return false;
}

} // namespace al
```



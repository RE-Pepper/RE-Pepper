

# File alCameraParamVision.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Camera**](dir_8bdd541d514c188acf6e59d710098364.md) **>** [**alCameraParamVision.cpp**](al_camera_param_vision_8cpp.md)

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



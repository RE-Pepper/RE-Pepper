

# File alCamera.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Camera**](dir_8bdd541d514c188acf6e59d710098364.md) **>** [**alCamera.cpp**](al_camera_8cpp.md)

[Go to the documentation of this file](al_camera_8cpp.md)


```C++
#include <Camera/alCamera.h>
#include <Camera/alCameraDashAngleTunerParam.h>
#include <Camera/alCameraParamVision.h>
#include <Camera/alCameraRotatorParam.h>
#include <Yaml/alByamlIter.h>

namespace al
{

#ifdef NON_MATCHING
// vtable
Camera::Camera( const char* name )
    : mName( name ), _8( sead::Vector3f::zero ), mPos( sead::Vector3f( 0, 500, 500 ) ),
      mTarget( sead::Vector3f::ey ), _2C( sead::Vector3f::ey ), mInterpoleFrame( 30 ),
      mVisionParam( nullptr ), mDashAngleTunerParam( nullptr ), mUnknownParam( nullptr ),
      mRotatorParam( nullptr )
{
        mDashAngleTunerParam = new CameraDashAngleTunerParam;
        mUnknownParam        = new CameraUnknownParam;
        mRotatorParam        = new CameraRotatorParam;
}

#endif

void Camera::load( const al::ByamlIter* ticket )
{
        ticket->tryGetIntByKey( &mInterpoleFrame, "InterpoleFrame" );
        if ( mInterpoleFrame < 0 )
                mInterpoleFrame = 30;
        if ( ticket->isExistKey( "VisionParam" ) )
        {
                mVisionParam = new CameraParamVision;
                mVisionParam->init( ticket );
        }
        mDashAngleTunerParam->init( ticket );
        mRotatorParam->init( ticket );
}

void Camera::v1()
{
}

void Camera::v2()
{
}

void Camera::v3()
{
}

void Camera::v4()
{
}

void Camera::v5()
{
}

void Camera::calc()
{
}

void Camera::v7()
{
}

} // namespace al
```





# File alCameraRotatorParam.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Camera**](dir_ae22786bedc4ead2a439ef673b994a37.md) **>** [**alCameraRotatorParam.cpp**](al_camera_rotator_param_8cpp.md)

[Go to the documentation of this file](al_camera_rotator_param_8cpp.md)


```C++
#include <Camera/alCameraRotatorParam.h>
#include <Yaml/alByamlIter.h>

namespace al
{

CameraRotatorParam::CameraRotatorParam() : mAngleMax( 30 )
{
}

void CameraRotatorParam::init( const ByamlIter* ticket )
{
        ByamlIter h;
        ticket->tryGetIterByKey( &h, "Rotator" );
        h.tryGetFloatByKey( &mAngleMax, "AngleMax" );
}

} // namespace al
```



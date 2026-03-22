

# File alCameraDashAngleTunerParam.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Camera**](dir_8bdd541d514c188acf6e59d710098364.md) **>** [**alCameraDashAngleTunerParam.cpp**](al_camera_dash_angle_tuner_param_8cpp.md)

[Go to the documentation of this file](al_camera_dash_angle_tuner_param_8cpp.md)


```C++
#include <Camera/alCameraDashAngleTunerParam.h>
#include <Yaml/alByamlIter.h>

namespace al
{

CameraDashAngleTunerParam::CameraDashAngleTunerParam() : mAddAngleMax( 15 ), mZoomOutOffsetMax( 200 )
{
}

void CameraDashAngleTunerParam::init( const ByamlIter* ticket )
{
        ByamlIter h;
        ticket->tryGetIterByKey( &h, "DashAngleTuner" );
        h.tryGetFloatByKey( &mAddAngleMax, "AddAngleMax" );
        h.tryGetFloatByKey( &mZoomOutOffsetMax, "ZoomOutOffsetMax" );
}

} // namespace al
```



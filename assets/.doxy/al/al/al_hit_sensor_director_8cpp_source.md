

# File alHitSensorDirector.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alHitSensorDirector.cpp**](al_hit_sensor_director_8cpp.md)

[Go to the documentation of this file](al_hit_sensor_director_8cpp.md)


```C++
#include <Execute/alExecuteTableHolder.h>
#include <HitSensor/alSensorHitGroup.h>
#include <LiveActor/alHitSensorDirector.h>

namespace al
{

HitSensorDirector::HitSensorDirector()
    : mPlayerHitGroup( nullptr ), mRideHitGroup( nullptr ), mEyeHitGroup( nullptr ),
      mSimpleHitGroup( nullptr ), mMapObjHitGroup( nullptr ), mCharacterHitGroup( nullptr )
{
        mPlayerHitGroup    = new SensorHitGroup( 16, "Player" );
        mRideHitGroup      = new SensorHitGroup( 128, "Ride" );
        mEyeHitGroup       = new SensorHitGroup( 512, "Eye" );
        mSimpleHitGroup    = new SensorHitGroup( 2048, "Simple" );
        mMapObjHitGroup    = new SensorHitGroup( 1024, "MapObj" );
        mCharacterHitGroup = new SensorHitGroup( 1024, "Character" );

        registerExecutorUser( this, "センサー" );
}

} // namespace al
```



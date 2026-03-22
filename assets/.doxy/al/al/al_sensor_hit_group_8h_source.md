

# File alSensorHitGroup.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**HitSensor**](dir_a2a99ef7263af19e42c28e75f0e41509.md) **>** [**alSensorHitGroup.h**](al_sensor_hit_group_8h.md)

[Go to the documentation of this file](al_sensor_hit_group_8h.md)


```C++
#pragma once

#include <HitSensor/alHitSensor.h>
#include <container/seadPtrArray.h>

namespace al
{

class SensorHitGroup
{
private:
        sead::PtrArray<HitSensor> mSensors;

public:
        void add( HitSensor* sensor );
        void remove( HitSensor* sensor );

public:
        SensorHitGroup( int, const char* name /* unused */ );
};

} // namespace al
```



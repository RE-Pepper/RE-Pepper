

# File alSensorHitGroup.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**HitSensor**](dir_c5bc830a30df7017e98410e84b00e200.md) **>** [**alSensorHitGroup.h**](al_sensor_hit_group_8h.md)

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



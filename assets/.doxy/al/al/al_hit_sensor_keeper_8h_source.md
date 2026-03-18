

# File alHitSensorKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alHitSensorKeeper.h**](al_hit_sensor_keeper_8h.md)

[Go to the documentation of this file](al_hit_sensor_keeper_8h.md)


```C++
#pragma once

#include <HitSensor/alHitSensor.h>
#include <container/seadPtrArray.h>

namespace al
{

class HitSensorKeeper
{
private:
        sead::PtrArray<HitSensor> mSensors;

public:
        HitSensor* getSensor( const char* name ) const;

public:
        void attackSensor();
        void validate();
        void invalidate();
        void validateBySystem();
        void invalidateBySystem();

        void update();
};

} // namespace al
```





# File alHitSensorDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alHitSensorDirector.h**](al_hit_sensor_director_8h.md)

[Go to the documentation of this file](al_hit_sensor_director_8h.md)


```C++
#pragma once

#include <Execute/alExecuteDirector.h>

namespace al
{
class SensorHitGroup;

class HitSensorDirector : public IUseExecutor
{
private:
        SensorHitGroup* mPlayerHitGroup;
        SensorHitGroup* mRideHitGroup;
        SensorHitGroup* mEyeHitGroup;
        SensorHitGroup* mSimpleHitGroup;
        SensorHitGroup* mMapObjHitGroup;
        SensorHitGroup* mCharacterHitGroup;

public:
        HitSensorDirector();
};

} // namespace al
```



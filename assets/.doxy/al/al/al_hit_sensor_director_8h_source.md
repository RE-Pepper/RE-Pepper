

# File alHitSensorDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alHitSensorDirector.h**](al_hit_sensor_director_8h.md)

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



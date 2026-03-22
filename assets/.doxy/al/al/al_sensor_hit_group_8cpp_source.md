

# File alSensorHitGroup.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**HitSensor**](dir_166101e35035935ea19b4cec6d2eed7d.md) **>** [**alSensorHitGroup.cpp**](al_sensor_hit_group_8cpp.md)

[Go to the documentation of this file](al_sensor_hit_group_8cpp.md)


```C++
#include <HitSensor/alSensorHitGroup.h>

namespace al
{

void SensorHitGroup::add( HitSensor* sensor )
{
        mSensors.pushBack( sensor );
}

} // namespace al
```



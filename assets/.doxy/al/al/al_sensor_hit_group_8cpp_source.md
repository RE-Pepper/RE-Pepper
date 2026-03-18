

# File alSensorHitGroup.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**HitSensor**](dir_132e8bbbb1839ed04e42ac9e1a233121.md) **>** [**alSensorHitGroup.cpp**](al_sensor_hit_group_8cpp.md)

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



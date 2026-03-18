

# File alSensorFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alSensorFunction.h**](al_sensor_function_8h.md)

[Go to the documentation of this file](al_sensor_function_8h.md)


```C++
#pragma once

#include <HitSensor/alSensorType.h>

namespace al
{
class LiveActor;
}

namespace alSensorFunction
{

al::SensorType findSensorTypeByName( const char* name );
void           updateHitSensorsAll( al::LiveActor* actor );

} // namespace alSensorFunction
```





# File alHitSensorFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alHitSensorFunction.h**](al_hit_sensor_function_8h.md)

[Go to the documentation of this file](al_hit_sensor_function_8h.md)


```C++
#pragma once

namespace al
{
class HitSensor;

bool isSensorName( HitSensor* sensor, const char* name );

bool isSensorPlayer( const HitSensor* sensor );
bool isSensorRide( const HitSensor* sensor );
bool isSensorEnemy( const HitSensor* sensor );
bool isSensorEnemyBody( const HitSensor* sensor );
bool isSensorEnemyAttack( const HitSensor* sensor );
bool isSensorSimple( const HitSensor* sensor );
bool isSensorMapObj( const HitSensor* sensor );

} // namespace al
```



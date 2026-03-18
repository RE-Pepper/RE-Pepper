

# File alHitSensorFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**LiveActor**](dir_8d17faa1063b24478b1232799869255d.md) **>** [**alHitSensorFunction.cpp**](al_hit_sensor_function_8cpp.md)

[Go to the documentation of this file](al_hit_sensor_function_8cpp.md)


```C++
#include <HitSensor/alHitSensor.h>
#include <LiveActor/alHitSensorFunction.h>
#include <Util/alStringUtil.h>

namespace al
{

bool isSensorName( HitSensor* sensor, const char* name )
{
        return isEqualString( sensor->getName(), name );
}

bool isSensorPlayer( const HitSensor* sensor )
{
        return sensor->getType() == SensorType_Player || sensor->getType() == SensorType_PlayerFireBall;
}

bool isSensorRide( const HitSensor* sensor )
{
        return sensor->getType() == SensorType_Ride;
}

bool isSensorEnemy( const HitSensor* sensor )
{
        return sensor->getType() == SensorType_Enemy || sensor->getType() == SensorType_EnemyBody ||
               sensor->getType() == SensorType_EnemyAttack ||
               sensor->getType() == SensorType_KillerMagnum || sensor->getType() == SensorType_Dossun;
}

bool isSensorEnemyBody( const HitSensor* sensor )
{
        return sensor->getType() == SensorType_EnemyBody;
}

bool isSensorEnemyAttack( const HitSensor* sensor )
{
        return sensor->getType() == SensorType_EnemyAttack;
}

bool isSensorSimple( const HitSensor* sensor )
{
        return sensor->getType() == SensorType_EnemySimple ||
               sensor->getType() == SensorType_MapObjSimple || sensor->getType() == SensorType_Bindable;
}

bool isSensorMapObj( const HitSensor* sensor )
{
        return sensor->getType() == SensorType_MapObj;
}

} // namespace al
```



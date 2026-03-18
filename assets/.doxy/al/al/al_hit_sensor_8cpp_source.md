

# File alHitSensor.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**HitSensor**](dir_132e8bbbb1839ed04e42ac9e1a233121.md) **>** [**alHitSensor.cpp**](al_hit_sensor_8cpp.md)

[Go to the documentation of this file](al_hit_sensor_8cpp.md)


```C++
#include <HitSensor/alHitSensor.h>
#include <HitSensor/alSensorHitGroup.h>

namespace al
{

void HitSensor::validate()
{
        if ( !mIsValid )
        {
                mIsValid = true;
                if ( mMaxSensorCount && mIsValidBySystem )
                        mSensorHitGroup->add( this );
        }
        mSensorCount = 0;
}

void HitSensor::invalidate()
{
        if ( mIsValid )
        {
                mIsValid = false;
                if ( mMaxSensorCount && mIsValidBySystem )
                        mSensorHitGroup->remove( this );
        }
        mSensorCount = 0;
}

void HitSensor::validateBySystem()
{
        if ( mIsValidBySystem )
                return;
        if ( mMaxSensorCount && mIsValid )
                mSensorHitGroup->add( this );
        mIsValidBySystem = true;
        mSensorCount     = 0;
}

void HitSensor::invalidateBySystem()
{
        if ( !mIsValidBySystem )
                return;
        if ( mMaxSensorCount && mIsValid )
                mSensorHitGroup->remove( this );
        mIsValidBySystem = false;
        mSensorCount     = 0;
}

} // namespace al
```



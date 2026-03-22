

# File alHitSensor.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**HitSensor**](dir_166101e35035935ea19b4cec6d2eed7d.md) **>** [**alHitSensor.cpp**](al_hit_sensor_8cpp.md)

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



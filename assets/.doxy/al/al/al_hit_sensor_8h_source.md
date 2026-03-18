

# File alHitSensor.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**HitSensor**](dir_c5bc830a30df7017e98410e84b00e200.md) **>** [**alHitSensor.h**](al_hit_sensor_8h.md)

[Go to the documentation of this file](al_hit_sensor_8h.md)


```C++
#pragma once

#include <HitSensor/alSensorType.h>
#include <math/seadMatrix.h>
#include <math/seadVector.h>

namespace al
{

class LiveActor;
class SensorHitGroup;

class HitSensor
{
        friend class HitSensorKeeper;

private:
        const char*      mName;
        SensorType       mSensorType;
        u32              _8;
        u32              _C;
        float            _10;
        float            mSensorRadius;
        u16              mMaxSensorCount;
        u16              mSensorCount;
        HitSensor**      mSensors;
        SensorHitGroup*  mSensorHitGroup;
        bool             mIsValidBySystem;
        bool             mIsValid;
        LiveActor*       mHostActor;
        sead::Vector3f*  mFollowPos;
        sead::Matrix34f* mFollowMtx;
        sead::Vector3f   _34;

public:
        const char* getName()
        {
                return mName;
        }

        LiveActor* getHost()
        {
                return mHostActor;
        }

        u32 getType() const
        {
                return mSensorType;
        }

        float getRadius() const
        {
                return mSensorRadius;
        }

        void validate();
        void invalidate();
        void validateBySystem();
        void invalidateBySystem();
        void update();
};

static_assert( sizeof( HitSensor ) == 0x40, "" );

bool isHitCylinderSensor( HitSensor*, HitSensor*, const sead::Vector3f&, float );

} // namespace al
```



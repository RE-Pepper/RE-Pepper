#pragma once

#include <HitSensor/alHitSensor.h>
#include <container/seadPtrArray.h>

namespace al
{

class HitSensorKeeper
{
private:
        sead::PtrArray<HitSensor> mSensors;

public:
        HitSensor* getSensor( const char* name ) const;

public:
        void attackSensor();
        void validate();
        void invalidate();
        void validateBySystem();
        void invalidateBySystem();

        void update();
};

} // namespace al

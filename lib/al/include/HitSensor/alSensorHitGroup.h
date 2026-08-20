#pragma once

#include <HitSensor/alHitSensor.h>
#include <container/seadPtrArray.h>

namespace al
{

class SensorHitGroup
{
private:
        sead::PtrArray<HitSensor> mSensors;

public:
        void add( HitSensor* sensor );
        void remove( HitSensor* sensor );

public:
        SensorHitGroup( int, const char* name /* unused */ );
};

} // namespace al

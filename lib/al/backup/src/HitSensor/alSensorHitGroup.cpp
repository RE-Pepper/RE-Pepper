#include <HitSensor/alSensorHitGroup.h>

namespace al
{

void SensorHitGroup::add( HitSensor* sensor )
{
        mSensors.pushBack( sensor );
}

} // namespace al

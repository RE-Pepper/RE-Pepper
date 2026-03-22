

# File alHitSensorKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alHitSensorKeeper.cpp**](al_hit_sensor_keeper_8cpp.md)

[Go to the documentation of this file](al_hit_sensor_keeper_8cpp.md)


```C++
#include <LiveActor/alHitSensorKeeper.h>
#include <LiveActor/alLiveActor.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Util/alStringUtil.h>

namespace al
{

#ifdef NON_MATCHING

// r5 <-> r6
void HitSensorKeeper::attackSensor()
{
        for ( int i = 0; i < mSensors.size(); i++ )
        {
                HitSensor* sensor = mSensors.unsafeAt( i );
                for ( int j = 0; j < sensor->mSensorCount; j++ )
                {
                        HitSensor* attacked = sensor->mSensors[ j ];
                        if ( !al::isDead( attacked->getHost() ) )
                                attacked->getHost()->attackSensor( sensor, attacked );
                }
        }
}
#endif

void HitSensorKeeper::validate()
{
        for ( int i = 0; i < mSensors.size(); i++ )
                mSensors.unsafeAt( i )->validate();
}

void HitSensorKeeper::invalidate()
{
        for ( int i = 0; i < mSensors.size(); i++ )
                mSensors.unsafeAt( i )->invalidate();
}

void HitSensorKeeper::validateBySystem()
{
        for ( int i = 0; i < mSensors.size(); i++ )
                mSensors.unsafeAt( i )->validateBySystem();
}

void HitSensorKeeper::invalidateBySystem()
{
        for ( int i = 0; i < mSensors.size(); i++ )
                mSensors.unsafeAt( i )->invalidateBySystem();
}

HitSensor* HitSensorKeeper::getSensor( const char* name ) const
{
        if ( mSensors.size() == 1 )
                return mSensors.unsafeAt( 0 );

        for ( int i = 0; i < mSensors.size(); i++ )
                if ( al::isEqualString( mSensors.unsafeAt( i )->getName(), name ) )
                        return mSensors.unsafeAt( i );
        return nullptr;
}

void HitSensorKeeper::update()
{
        for ( int i = 0; i < mSensors.size(); i++ )
                mSensors.unsafeAt( i )->update();
}

} // namespace al
```



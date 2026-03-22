#pragma once

#include <MapObj/alMapObjActor.h>

class FireBall : public al::MapObjActor
{
public:
        void exeShot();

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void attackSensor( al::HitSensor* me, al::HitSensor* other );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        FireBall( const sead::SafeString& name );
};

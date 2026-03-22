#pragma once

#include <MapObj/alMapObjActor.h>

class EnemyStateBlowDown;

class Fugumannen : public al::MapObjActor
{
private:
        float               mRailMoveSpeed;
        EnemyStateBlowDown* mStateBlowDown;

public:
        void exeMove();
        void exeMove2();
        void exeBlowDown();

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void attackSensor( al::HitSensor* me, al::HitSensor* other );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        Fugumannen( const sead::SafeString& name );
};

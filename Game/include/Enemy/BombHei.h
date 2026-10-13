#pragma once

#include <MapObj/alMapObjActor.h>

class BombHei : public al::MapObjActor
{
private:
        u8    _60[ 0x20 ];
        float _80;
        bool  _84;
        void* _88;

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void makeActorAppeared();
        virtual void attackSensor( al::HitSensor* me, al::HitSensor* other );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        BombHei( const sead::SafeString& name );
};

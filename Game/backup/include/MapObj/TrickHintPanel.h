#pragma once

#include <MapObj/alMapObjActor.h>

class TrickHintPanel : public al::MapObjActor
{
private:
        u32  _96;
        bool mPlayedSound;

public:
        void exeWait();
        void exeOn();
        void exenrv3();
        void exeOff();

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        TrickHintPanel( const sead::SafeString& name );
};

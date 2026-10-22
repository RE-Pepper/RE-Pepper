#pragma once

#include <MapObj/alMapObjActor.h>



class FallMapParts : public al::MapObjActor
{
private:
        sead::Vector3f mStartTrans;
        int            mFallFrames;
        bool           _70;

public:
        void exeAppear();
        void exeWait();
        void exeFallSign();
        void exeFall();
        void exeEnd();

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        FallMapParts( const sead::SafeString& name );
};

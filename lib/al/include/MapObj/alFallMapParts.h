#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class FallMapParts : public MapObjActor
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
        virtual void init( const ActorInitInfo& info );
        virtual bool receiveMsg( u32 msg, HitSensor* other, HitSensor* me );

public:
        FallMapParts( const sead::SafeString& name );
};

} // namespace al

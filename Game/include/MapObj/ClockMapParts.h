#pragma once

#include <MapObj/alMapObjActor.h>

class ClockMapParts : public al::MapObjActor
{
private:
        sead::Quatf _60;
        int         _70;
        float       _74;
        int         _78;
        int         _7C;
        int         _80;

public
        void exeStandBy();
        void exeRotateSign();
        void exeRotate();
        void exeWait();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        ClockMapParts( const sead::SafeString& name );
};

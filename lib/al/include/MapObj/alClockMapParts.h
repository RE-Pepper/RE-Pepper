#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class ClockMapParts : public MapObjActor
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
        virtual void init( const ActorInitInfo& info );

public:
        ClockMapParts( const sead::SafeString& name );
};

} // namespace al

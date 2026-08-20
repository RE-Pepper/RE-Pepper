#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class Sky : public MapObjActor
{
private:
        const sead::Vector3f* mCameraTransPtr;

public:
        virtual void init( const ActorInitInfo& info );
        virtual void calcAnim();

public:
        Sky( const char* name );
};

} // namespace al

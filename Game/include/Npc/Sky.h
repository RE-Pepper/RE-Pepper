#pragma once

#include <MapObj/alMapObjActor.h>



class Sky : public al::MapObjActor
{
private:
        const sead::Vector3f* mCameraTransPtr;

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void calcAnim();

public:
        Sky( const char* name );
};

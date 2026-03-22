#pragma once

#include <MapObj/alMapObjActor.h>

class PeachRope : public al::MapObjActor
{
public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void kill();

public:
        PeachRope( const sead::SafeString& name );
};

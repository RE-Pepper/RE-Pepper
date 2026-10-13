#pragma once

#include <MapObj/alMapObjActor.h>

class RailDot : public al::MapObjActor
{
public:
        void exeWait();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        RailDot( const sead::SafeString& name );
};

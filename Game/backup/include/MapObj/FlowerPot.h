#pragma once

#include <MapObj/alMapObjActor.h>

class FlowerPot : public al::MapObjActor
{
public:
        void exeWait();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        FlowerPot( const sead::SafeString& name );
};

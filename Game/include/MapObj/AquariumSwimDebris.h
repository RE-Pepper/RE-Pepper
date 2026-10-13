#pragma once

#include <MapObj/alMapObjActor.h>

class AquariumSwimDebris : public al::MapObjActor
{
public:
        void exeAppear();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        AquariumSwimDebris( const sead::SafeString& name );
};

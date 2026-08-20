#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class FixMapParts : public MapObjActor
{
public:
        FixMapParts( const sead::SafeString& name );

        virtual void init( const ActorInitInfo& info );
        virtual void appear();
};

} // namespace al

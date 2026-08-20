#pragma once

#include <LiveActor/alLiveActor.h>
#include <prim/seadSafeString.h>

namespace al
{

class MapObjActor : public LiveActor
{
public:
        MapObjActor( const sead::SafeString& name );
};

} // namespace al

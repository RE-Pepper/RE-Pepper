

# File alActorInitInfo.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alActorInitInfo.h**](al_actor_init_info_8h.md)

[Go to the documentation of this file](al_actor_init_info_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <prim/seadSafeString.h>

namespace al
{

class LiveActorKit;
class LayoutInitInfo;

class ActorInitInfo
{
public:
        const PlacementInfo* mPlacementInfo;
        void*                _4;
        void*                _8;
        void*                _C;
        void*                _10;
        int                  mViewId;

        ActorInitInfo();

        void initViewIdHost( const PlacementInfo* placement, const ActorInitInfo& hostInfo );
        void initViewIdSelf( const PlacementInfo* placement, const ActorInitInfo& hostInfo );

        void initNew( const PlacementInfo* placement, const ActorInitInfo& baseInfo );

        friend const PlacementInfo& getPlacementInfo( const ActorInitInfo& info );
};

inline const PlacementInfo& getPlacementInfo( const ActorInitInfo& info )
{
        return *info.mPlacementInfo;
}

void initActorInitInfo( ActorInitInfo* info, const PlacementInfo* placement, const LayoutInitInfo& layoutInfo, LiveActorKit* );

} // namespace al
```



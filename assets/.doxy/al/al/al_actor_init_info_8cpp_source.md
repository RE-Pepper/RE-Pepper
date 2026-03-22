

# File alActorInitInfo.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alActorInitInfo.cpp**](al_actor_init_info_8cpp.md)

[Go to the documentation of this file](al_actor_init_info_8cpp.md)


```C++
#include <LiveActor/alActorInitInfo.h>
#include <LiveActor/alLiveActor.h>
#include <Placement/alPlacementFunction.h>

namespace al
{

ActorInitInfo::ActorInitInfo()
    : mPlacementInfo( nullptr ), _4( nullptr ), _8( nullptr ), _C( nullptr ), _10( nullptr ), mViewId( -1 )
{
}

void ActorInitInfo::initViewIdHost( const PlacementInfo* placement, const ActorInitInfo& hostInfo )
{
        mPlacementInfo = placement;
        _4             = hostInfo._4;
        _8             = hostInfo._8;
        _10            = hostInfo._10;
        mViewId        = hostInfo.mViewId;
}

void ActorInitInfo::initViewIdSelf( const PlacementInfo* placement, const ActorInitInfo& hostInfo )
{
        mPlacementInfo = placement;
        _4             = hostInfo._4;
        _8             = hostInfo._8;
        _10            = hostInfo._10;
        mViewId        = alPlacementFunction::getClippingViewId( *placement );
}

#ifdef NON_MATCHING

// registers used when copying from base info
void initActorInitInfo( ActorInitInfo* info, const PlacementInfo* placement, const ActorInitInfo& baseInfo )
{
        info->initViewIdSelf( placement, baseInfo );
}
#endif

} // namespace al
```



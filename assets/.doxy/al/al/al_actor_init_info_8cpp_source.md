

# File alActorInitInfo.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**LiveActor**](dir_8d17faa1063b24478b1232799869255d.md) **>** [**alActorInitInfo.cpp**](al_actor_init_info_8cpp.md)

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



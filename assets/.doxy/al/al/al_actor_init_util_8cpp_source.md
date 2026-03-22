

# File alActorInitUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alActorInitUtil.cpp**](al_actor_init_util_8cpp.md)

[Go to the documentation of this file](al_actor_init_util_8cpp.md)


```C++
#include <LiveActor/alActorInitInfo.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActor.h>
#include <Placement/alPlacementFunction.h>
#include <Util/alStringUtil.h>

namespace al
{

#pragma push
#pragma no_inline

#ifdef NON_MATCHING
static void initActorImpl( LiveActor* actor, const ActorInitInfo& info, const sead::SafeString& objectName, const sead::SafeString& archivePath, const char* suffix = nullptr )
{ // placeholder
}
#endif

#pragma pop

#ifdef NON_MATCHING

// SafeString construction backwards
void initActor( LiveActor* actor, const ActorInitInfo& info )
{
        const char* objectName = nullptr;
        tryGetObjectName( &objectName, info );
        initActorImpl( actor, info, objectName, StringTmp<256>( "ObjectData/%s", objectName ) );
}

// ???
void initActorWithArchiveName( LiveActor* actor, const ActorInitInfo& info, const sead::SafeString& archiveName, const char* suffix )
{
        initActorImpl( actor, info, archiveName.cstr(), StringTmp<256>( "ObjectData/%s", archiveName.cstr() ), suffix );
}
#endif

void initCreateActorNoPlacementInfo( LiveActor* actor, const ActorInitInfo& hostInfo )
{
        PlacementInfo placementInfo;
        ActorInitInfo info;
        info.initViewIdHost( &placementInfo, hostInfo );
        actor->init( info );
}

void initCreateActorWithPlacementInfo( LiveActor* actor, const ActorInitInfo& hostInfo )
{
        actor->init( hostInfo );
}

} // namespace al
```



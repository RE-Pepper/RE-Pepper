

# File alActorInitUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alActorInitUtil.h**](al_actor_init_util_8h.md)

[Go to the documentation of this file](al_actor_init_util_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <prim/seadSafeString.h>

namespace al
{
class LiveActor;
class ActorInitInfo;

void initActor( LiveActor* actor, const ActorInitInfo& info );
void initActorWithArchiveName( LiveActor* actor, const ActorInitInfo& info, const sead::SafeString& archiveName, const char* suffix = nullptr );
void initActorWithArchiveNameNoPlacementInfo( LiveActor* actor, const ActorInitInfo& info, const sead::SafeString& archiveName, const char* suffix = nullptr );
void initMapPartsActor( LiveActor* actor, const ActorInitInfo& info );

void initCreateActorNoPlacementInfo( LiveActor* actor, const ActorInitInfo& hostInfo );
void initCreateActorWithPlacementInfo( LiveActor* actor, const ActorInitInfo& hostInfo );

} // namespace al
```



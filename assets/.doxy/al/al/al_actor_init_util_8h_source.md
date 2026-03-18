

# File alActorInitUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alActorInitUtil.h**](al_actor_init_util_8h.md)

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



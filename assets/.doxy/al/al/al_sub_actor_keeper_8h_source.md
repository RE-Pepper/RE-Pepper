

# File alSubActorKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alSubActorKeeper.h**](al_sub_actor_keeper_8h.md)

[Go to the documentation of this file](al_sub_actor_keeper_8h.md)


```C++
#pragma once

#include <container/seadPtrArray.h>

class alSubActorFunction;

namespace al
{

class LiveActor;
class ActorInitInfo;

class SubActorKeeper
{
        friend class ::alSubActorFunction;

private:
        struct Entry
        {
                LiveActor* actor;
                void*      _4;
                u32        _8;
        };

        LiveActor* const      mParent;
        sead::PtrArray<Entry> mSubActors;

public:
        static SubActorKeeper* tryCreate( al::LiveActor* actor, const al::ActorInitInfo& info, const char*, int );

private:
        SubActorKeeper( al::LiveActor* actor, const al::ActorInitInfo& info, const char*, int );
};

} // namespace al
```



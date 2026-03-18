

# File alSubActorKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alSubActorKeeper.h**](al_sub_actor_keeper_8h.md)

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





# File alLiveActorGroup.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alLiveActorGroup.h**](al_live_actor_group_8h.md)

[Go to the documentation of this file](al_live_actor_group_8h.md)


```C++
#pragma once

#include <LiveActor/alLiveActor.h>
#include <container/seadPtrArray.h>

namespace al
{

class LiveActorGroup
{
private:
        const char* const         mName;
        sead::PtrArray<LiveActor> mActors;

public:
        void killAll();
        void makeActorDeadAll();

        template <typename T>
        sead::PtrArray<T>& getArray()
        {
                return reinterpret_cast<sead::PtrArray<T>&>( mActors );
        }

public:
        virtual void registerActor( LiveActor* actor );

public:
        LiveActorGroup( const char* name, int bufSize );
};

} // namespace al
```



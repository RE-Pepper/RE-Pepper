

# File alLiveActorGroup.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alLiveActorGroup.h**](al_live_actor_group_8h.md)

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



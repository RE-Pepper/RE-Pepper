

# File WalkerStateWander.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Enemy**](dir_e35196509c323c9bb4cd921cf1b24d53.md) **>** [**WalkerStateWander.h**](_walker_state_wander_8h.md)

[Go to the documentation of this file](_walker_state_wander_8h.md)


```C++
#pragma once

#include <Nerve/alActorStateBase.h>

class WalkerStateParam;
class WalkerStateWanderParam;

class WalkerStateWander : public al::ActorStateBase
{
private:
        sead::Vector3f*               mFrontPtr;
        void*                         _14;
        const WalkerStateParam*       mWalkerParam;
        const WalkerStateWanderParam* mWanderParam;

public:
        WalkerStateWander( al::LiveActor* host, sead::Vector3f* frontPtr, const WalkerStateParam* walkerParam, const WalkerStateWanderParam* wanderParam );
};
```



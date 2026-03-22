

# File WalkerStateChase.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Enemy**](dir_e35196509c323c9bb4cd921cf1b24d53.md) **>** [**WalkerStateChase.h**](_walker_state_chase_8h.md)

[Go to the documentation of this file](_walker_state_chase_8h.md)


```C++
#pragma once

#include <LiveActor/alLiveActor.h>
#include <Nerve/alActorStateBase.h>

class WalkerStateChaseParam;
class WalkerStateParam;

class WalkerStateChase : public al::ActorStateBase
{
private:
        sead::Vector3f*              mFrontPtr;
        const WalkerStateParam*      mWalkParam;
        const WalkerStateChaseParam* mRunParam;
        bool                         _1C;
        void*                        _20;

public:
        void exeStart();

public:
        WalkerStateChase( al::LiveActor* host, sead::Vector3f* frontPtr, const WalkerStateParam* walkParam, const WalkerStateChaseParam* runParam, bool );
};
```



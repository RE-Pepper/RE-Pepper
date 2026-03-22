

# File EnemyStateBlowDown.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Enemy**](dir_e35196509c323c9bb4cd921cf1b24d53.md) **>** [**EnemyStateBlowDown.h**](_enemy_state_blow_down_8h.md)

[Go to the documentation of this file](_enemy_state_blow_down_8h.md)


```C++
#pragma once

#include <Nerve/alActorStateBase.h>
#include <math/seadVector.h>

class EnemyStateBlowDownParam;

class EnemyStateBlowDown : public al::ActorStateBase
{
private:
        EnemyStateBlowDownParam* mParam;
        sead::Vector3f           _14;
        const char*              mAnimName;
        void*                    _24;

public:
        EnemyStateBlowDown( al::LiveActor* host, EnemyStateBlowDownParam* blowDownParam, const char*, int );
};
```



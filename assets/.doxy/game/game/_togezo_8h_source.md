

# File Togezo.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Enemy**](dir_e35196509c323c9bb4cd921cf1b24d53.md) **>** [**Togezo.h**](_togezo_8h.md)

[Go to the documentation of this file](_togezo_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class WalkerStateWander;
class WalkerStateChase;
class EnemyStateBlowDown;

class Togezo : public al::MapObjActor
{
private:
        WalkerStateWander*  mWanderState;
        WalkerStateChase*   mChaseState;
        EnemyStateBlowDown* mBlowDownState;

public:
        void exeWander();
        void exeTurn();
        void exeSearch();
        void exeChase();
        void exeAttack();
        void exeBlowDown();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        Togezo( const sead::SafeString& name );
};
```



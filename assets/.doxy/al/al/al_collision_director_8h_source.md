

# File alCollisionDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Collision**](dir_b64277db147a0cb833174dd0bf4617cc.md) **>** [**alCollisionDirector.h**](al_collision_director_8h.md)

[Go to the documentation of this file](al_collision_director_8h.md)


```C++
#pragma once

#include <Execute/alExecuteDirector.h>

namespace al
{

class CollisionDirector : public IUseExecutor
{
private:
        void* _4;
        int   _8;
        int   _C;
        void* _10;
        void* _14;
        void* _18;

public:
        void endInit();

public:
        virtual void execute();

public:
        CollisionDirector();
};

} // namespace al
```



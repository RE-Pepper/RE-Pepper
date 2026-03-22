

# File alCollisionParts.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Collision**](dir_b64277db147a0cb833174dd0bf4617cc.md) **>** [**alCollisionParts.h**](al_collision_parts_8h.md)

[Go to the documentation of this file](al_collision_parts_8h.md)


```C++
#pragma once

#include <math/seadMatrix.h>

namespace al
{
class KCollisionServer;
class CollisionParts;

class CollisionParts
{
private:
        int               _0;
        int               _4;
        CollisionParts*   _8;
        int               _C;
        int               _10;
        u8                _14[ 0xf0 ];
        float             _104;
        float             _108;
        float             _10C;
        float             _110;
        float             _114;
        int               _118;
        KCollisionServer* mCollisionServer;
        int               _120;
        int               _124;
        sead::Vector3f    _128;
        sead::Vector3f    _134;
        bool              _140;
        bool              _141;
        bool              _142;
        bool              _143;
        bool              _144;

public:
        void syncMtx( const sead::Matrix34f& );

public:
        CollisionParts( void* kclData, const void* paData );
};

} // namespace al
```



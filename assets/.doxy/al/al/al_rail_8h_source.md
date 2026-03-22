

# File alRail.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Rail**](dir_c8bcdc1e1ae46381fd1d0b5e3e0c3157.md) **>** [**alRail.h**](al_rail_8h.md)

[Go to the documentation of this file](al_rail_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <math/seadVector.h>

namespace al
{

class Rail
{
private:
        int  _0;
        int  _4;
        int  _8;
        int  _C;
        bool mIsClosed;

public:
        bool isClosed() const
        {
                return mIsClosed;
        }

        void init( const PlacementInfo& info );

        float getTotalLength() const;
        float normalizeLength( float ) const;
        void  calcPosDir( sead::Vector3f*, sead::Vector3f*, float );
        float calcNearestRailPosCoord( const sead::Vector3f&, float );

public:
        Rail();
};

} // namespace al
```



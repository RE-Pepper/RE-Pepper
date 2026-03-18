

# File alRail.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Rail**](dir_eddceeca1a9539e4ec5247c1a556acdf.md) **>** [**alRail.h**](al_rail_8h.md)

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



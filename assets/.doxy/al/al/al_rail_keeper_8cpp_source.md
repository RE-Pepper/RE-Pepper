

# File alRailKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Rail**](dir_6ff4c1b13859b82bf8a5d6f47c0db9b6.md) **>** [**alRailKeeper.cpp**](al_rail_keeper_8cpp.md)

[Go to the documentation of this file](al_rail_keeper_8cpp.md)


```C++
#include <Placement/alPlacementFunction.h>
#include <Rail/alRail.h>
#include <Rail/alRailKeeper.h>
#include <Rail/alRailRider.h>

namespace al
{

RailKeeper::RailKeeper( const PlacementInfo& info ) : mRail( nullptr ), mRailRider( nullptr )
{
        mRail = new Rail;
        mRail->init( info );
        mRailRider = new RailRider( mRail );
}

RailKeeper* tryCreateRailKeeper( const PlacementInfo& info )
{
        PlacementInfo railIter;
        if ( tryGetRailIter( &railIter, info ) )
                return new RailKeeper( railIter );
        return nullptr;
}

bool RailKeeper::isExistRail() const
{
        return mRail != nullptr;
}

} // namespace al
```



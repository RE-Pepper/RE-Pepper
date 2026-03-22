

# File alRailKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Rail**](dir_7704832a95887b8dfaac4c9470889cbe.md) **>** [**alRailKeeper.cpp**](al_rail_keeper_8cpp.md)

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



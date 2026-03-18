

# File alRailKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Rail**](dir_eddceeca1a9539e4ec5247c1a556acdf.md) **>** [**alRailKeeper.h**](al_rail_keeper_8h.md)

[Go to the documentation of this file](al_rail_keeper_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>

namespace al
{
class Rail;
class RailRider;

class RailKeeper
{
private:
        Rail*      mRail;
        RailRider* mRailRider;

public:
        Rail* getRail()
        {
                return mRail;
        }

        RailRider* getRailRider()
        {
                return mRailRider;
        }

        bool isExistRail() const;

public:
        friend RailKeeper* tryCreateRailKeeper( const PlacementInfo& info );

private:
        RailKeeper( const PlacementInfo& info );
};

RailKeeper* tryCreateRailKeeper( const PlacementInfo& info );

} // namespace al
```



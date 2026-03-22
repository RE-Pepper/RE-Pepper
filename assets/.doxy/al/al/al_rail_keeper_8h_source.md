

# File alRailKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Rail**](dir_c8bcdc1e1ae46381fd1d0b5e3e0c3157.md) **>** [**alRailKeeper.h**](al_rail_keeper_8h.md)

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



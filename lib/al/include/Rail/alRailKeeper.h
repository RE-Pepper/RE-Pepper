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
